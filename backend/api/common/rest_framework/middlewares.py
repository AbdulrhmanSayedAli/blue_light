import json
from rest_framework.response import Response
from common.rest_framework.pagination import PAGINATION_FLAG
from common.response_templates import TEMPLATE_FLAG, success_response, fail_response


class ResponseCoordinatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response: Response = self.get_response(request)
        if not request.path.startswith("/api/") or not response.headers.get("Content-Type") == "application/json":
            return response

        response_data = json.loads(response.content)

        if TEMPLATE_FLAG not in response_data:
            if 200 <= response.status_code < 300:
                if isinstance(response_data, dict) and response_data.pop(PAGINATION_FLAG, None):
                    new_response_data = success_response({}, code=response.status_code)
                    new_response_data.update(response_data)

                    # This line just to make the results as lower as possible in the response
                    # Deleting This line will not effect any thing
                    new_response_data["results"] = new_response_data.pop("results")

                    response_data = new_response_data
                else:
                    response_data = success_response(response_data, code=response.status_code)

            elif response.status_code == 400:
                if isinstance(response_data, dict):
                    message = response_data.pop("non_field_errors", None)
                    fields_errors = response_data

                elif isinstance(response_data, list):
                    message = response_data
                    fields_errors = {}

                if isinstance(message, list):
                    message = ",".join(message)

                response_data = fail_response(message=message, fields_errors=fields_errors, code=response.status_code)
            else:
                response_data = fail_response(message=response_data["detail"], code=response.status_code)

        response_data.pop(TEMPLATE_FLAG, None)
        response.content = json.dumps(response_data)
        return response
