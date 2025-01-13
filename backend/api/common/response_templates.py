TEMPLATE_FLAG = "_______#IS_TEMPLATE#_______"


def response_template(data, message, fields_errors, code):
    return {
        "code": code,
        "message": message,
        "fields_errors": fields_errors,
        "results": data,
        TEMPLATE_FLAG: True,
    }


def success_response(data, message="Success.", code=None):
    return response_template(data, message, None, code)


def fail_response(message="Fail.", fields_errors=None, code=None):
    return response_template(None, message, fields_errors, code)
