from common.audit.serializer import AuditSerializer
from .models import Order, OrderCourse
from users.serializers import GetUserSerializer
from common.rest_framework.serializers import CustomImageSerializerField
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from courses.serializers import CourseListSerializer


class PostOrderSerializer(AuditSerializer):
    class Meta:
        model = Order
        fields = (
            "payment_image",
            "payment_code",
        )

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        if not validated_data.get("payment_image", None) and not validated_data.get("payment_code", None):
            raise serializers.ValidationError(_("payment_image or payment_code are required."))

        validated_data["user"] = self.context["request"].user
        return validated_data

    def to_representation(self, instance):
        return OrderSerializer(instance, context=self.context).data


class OrderCourseSerializer(AuditSerializer):
    class Meta:
        model = OrderCourse
        fields = (
            "id",
            "course",
            "include_videos",
            "include_files",
            "include_quizzes",
            "price",
            "expires_at",
            "is_expired",
        )

    course = CourseListSerializer()


class OrderSerializer(AuditSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "payment_status",
            "payment_image",
            "payment_code",
            "price",
            "order_courses",
        )

    user = GetUserSerializer()
    payment_image = CustomImageSerializerField()
    order_courses = OrderCourseSerializer(many=True)


class OrderListSerializer(AuditSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "payment_status",
            "payment_image",
            "payment_code",
            "price",
        )
