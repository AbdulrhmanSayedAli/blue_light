from rest_framework import serializers


class CustomImageSerializerField(serializers.ImageField):
    def to_representation(self, value):
        if value.name and value.name.startswith("http"):
            return value.name
        return super().to_representation(value)

    def to_internal_value(self, data):
        """
        Handle both file and URL inputs.
        """
        if isinstance(data, str) and data.startswith("http"):
            return data
        return super().to_internal_value(data)


class CustomFileSerializerField(serializers.FileField):
    def to_representation(self, value):
        if value.name and value.name.startswith("http"):
            return value.name
        return super().to_representation(value)

    def to_internal_value(self, data):
        """
        Handle both file and URL inputs.
        """
        if isinstance(data, str) and data.startswith("http"):
            return data
        return super().to_internal_value(data)
