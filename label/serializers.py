from rest_framework import serializers

from label.models import Label


class LabelSerializer(serializers.Serializer):
    guid = serializers.UUIDField(read_only=True, source="guid.hex")
    user_guid = serializers.CharField(required=False, source="user.guid.hex")
    title = serializers.CharField(required=True, max_length=120)

    def create(self, validated_data):
        return Label.objects.create(**validated_data)
