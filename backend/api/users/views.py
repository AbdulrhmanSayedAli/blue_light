from rest_framework.viewsets import ReadOnlyModelViewSet
from users.models import City, Univeristy, Specialization
from users.serializers import (
    CitySerializer,
    RegisterSerializer,
    UniveristySerializer,
    SpecializationSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from myauth.views import createToken
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


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


class ProfileView(RetrieveAPIView, UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user
