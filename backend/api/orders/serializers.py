from common.audit.serializer import AuditSerializer
from .models import Order, OrderCourse
from users.serializers import GetUserSerializer
from common.rest_framework.serializers import CustomImageSerializerField
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from courses.serializers import CourseSerializer
from datetime import timedelta
from decimal import Decimal
from django.utils import timezone
from rest_framework import serializers


class OrderCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCourse
        fields = ["course", "include_videos", "include_files", "include_quizzes"]

    def validate(self, data):
        include_videos = data.get("include_videos", False)
        include_files = data.get("include_files", False)
        include_quizzes = data.get("include_quizzes", False)

        if not (include_videos or include_files or include_quizzes):
            raise serializers.ValidationError(
                _("At least one of include_videos, include_files, or include_quizzes must be true.")
            )

        if include_videos:
            if not include_files:
                raise serializers.ValidationError(
                    {"include_files": "This field must be True when include_videos is True."}
                )
            if not include_quizzes:
                raise serializers.ValidationError(
                    {"include_quizzes": "This field must be True when include_videos is True."}
                )
        return data


class OrderCreateSerializer(serializers.ModelSerializer):
    order_courses = OrderCourseCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ["payment_image", "payment_code", "order_courses"]

    payment_image = CustomImageSerializerField(allow_null=True, required=False)

    def validate_order_courses(self, value):
        """Ensure that the order_courses list is not empty."""
        if not value:
            raise serializers.ValidationError(_("The order_courses list cannot be empty."))
        return value

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
            price = 0
            include_videos = oc_data.get("include_videos", False)
            include_files = oc_data.get("include_files", False)
            include_quizzes = oc_data.get("include_quizzes", False)

            if include_videos:
                price += Decimal(str(course.videos_price))

            if include_files:
                price += Decimal(str(course.files_price))

            if include_quizzes:
                price += Decimal(str(course.quizzes_price))

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

    course = CourseSerializer()


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
            "order_courses",
        )

    order_courses = OrderCourseSerializer(many=True)
