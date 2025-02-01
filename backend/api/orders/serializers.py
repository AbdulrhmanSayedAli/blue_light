from common.audit.serializer import AuditSerializer
from .models import Order, OrderCourse
from users.serializers import GetUserSerializer
from common.rest_framework.serializers import CustomImageSerializerField
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from courses.serializers import CourseListSerializer
from datetime import timedelta
from decimal import Decimal
from django.utils import timezone
from rest_framework import serializers


class OrderCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCourse
        fields = ["course", "include_videos", "include_files", "include_quizzes"]

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if validated_data.get("include_videos", False):
            if not validated_data.get("include_files", False):
                raise serializers.ValidationError(
                    {"include_files": _("This field must be True when include_videos is True.")}
                )
            if not validated_data.get("include_quizzes", False):
                raise serializers.ValidationError(
                    {"include_quizzes": _("This field must be True when include_videos is True.")}
                )
        return validated_data


class OrderCreateSerializer(serializers.ModelSerializer):
    order_courses = OrderCourseCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ["payment_image", "payment_code", "order_courses"]

    payment_image = CustomImageSerializerField(allow_null=True, required=False)

    def validate(self, data):
        if not data.get("payment_image") and not data.get("payment_code"):
            raise serializers.ValidationError(_("Either payment_image or payment_code must be provided."))
        return data

    def create(self, validated_data):
        order_courses_data = validated_data.pop("order_courses")
        user = self.context["request"].user

        order = Order.objects.create(user=user, **validated_data)

        for oc_data in order_courses_data:
            course = oc_data["course"]
            price = Decimal(str(course.price))
            expires_at = timezone.now() + timedelta(days=course.duration_in_days)
            OrderCourse.objects.create(
                order=order,
                course=course,
                include_videos=oc_data.get("include_videos", False),
                include_files=oc_data.get("include_files", False),
                include_quizzes=oc_data.get("include_quizzes", False),
                price=price,
                expires_at=expires_at,
            )

        return order

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
