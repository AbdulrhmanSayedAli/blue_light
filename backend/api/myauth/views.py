from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from knox.models import AuthToken
from rest_framework.response import Response
from myauth.serializers import LoginSerializer
from users.serializers import GetUserSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


def createToken(user):
    instance, token = AuthToken.objects.create(user)
    return token


class LoginView(KnoxLoginView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary="Login with phone_number, device_id, and password",
        operation_description="Authenticate a user using phone_number, device_id, and password. "
        "Returns a token and user details if successful.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["phone_number", "device_id", "password"],
            properties={
                "phone_number": openapi.Schema(type=openapi.TYPE_STRING, description="The phone number of the user"),
                "device_id": openapi.Schema(type=openapi.TYPE_STRING, description="Unique device identifier"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, description="User's password"),
            },
        ),
        responses={200: ""},
    )
    def post(self, request):
        phone_number = request.data.get("phone_number")
        device_id = request.data.get("device_id")
        password = request.data.get("password")

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, username=phone_number, password=password, device_id=device_id)
        if user:
            serializer = GetUserSerializer(user)
            return Response({"token": createToken(user), "user": serializer.data})

        raise ValidationError(_("Invalid login."))
