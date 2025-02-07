from django.db import IntegrityError
from common.audit.serializer import AuditSerializer
from .models import Rate


class RateSerializer(AuditSerializer):
    class Meta:
        model = Rate
        fields = (
            "performance_of_the_application",
            "clarity_and_variety_of_materials",
            "response_and_interaction_of_the_trainer",
            "courses_helped_you",
            "notes",
        )

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        try:
            return super().create(validated_data)
        except IntegrityError:
            return self.update(Rate.objects.get(user=user), validated_data)
