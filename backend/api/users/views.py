from rest_framework.viewsets import ReadOnlyModelViewSet
from users.models import City, Univeristy, Specialization
from users.serializers import (
    CitySerializer,
    RegisterSerializer,
    UniveristySerializer,
    SpecializationSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ForgotPasswordSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from myauth.views import createToken
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import DeviceSerializer
from .models import User
from rest_framework.serializers import ValidationError
from safedelete.models import HARD_DELETE


class CityViewSet(ReadOnlyModelViewSet):
    model = City
    queryset = City.objects.all()
    serializer_class = CitySerializer
    search_fields = ["name"]
    ordering_fields = ["name"]


class UniveristyViewSet(ReadOnlyModelViewSet):
    model = Univeristy
    queryset = Univeristy.objects.all()
    serializer_class = UniveristySerializer
    search_fields = ["name"]
    ordering_fields = ["name"]


class SpecializationViewSet(ReadOnlyModelViewSet):
    model = Specialization
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]


class RegisterView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_summary="Register a new user",
        operation_description="Register a new user with phone_number, device_id, password, and other details.",
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response(
                description="User registered successfully",
                schema=RegisterSerializer,  # Use the serializer as the response schema
            ),
            400: openapi.Response(
                description="Invalid input data",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    additional_properties=openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                ),
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"token": createToken(user), **serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(UpdateAPIView):
    http_method_names = ["put"]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class ForgotPasswordView(UpdateAPIView):
    permission_classes = [AllowAny]
    http_method_names = ["put"]
    serializer_class = ForgotPasswordSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self):
        data = self.request.data
        phone_number = data.get("phone_number", None)
        device_id = data.get("device_id", None)
        user = User.objects.filter(phone_number=phone_number)
        if not user.exists():
            raise ValidationError("user not found")
        user = user.first()
        if user.device_id != device_id:
            raise ValidationError("user id doesnt match")
        print(user)
        return user


class ProfileView(RetrieveAPIView, UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


class DeviceCreateView(CreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.history.all().delete()
        user.delete()
        user.delete(force_policy=HARD_DELETE)
        return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
