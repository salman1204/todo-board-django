from rest_framework import serializers

from label.models import Label
from ticket.models import Ticket


class TicketSerializer(serializers.Serializer):
    guid = serializers.UUIDField(read_only=True, source="guid.hex")
    user_guid = serializers.CharField(required=False, source="user.guid.hex")
    label = serializers.CharField(required=True, source="label.guid.hex")
    label_title = serializers.CharField(required=False, source="label.title")
    title = serializers.CharField(required=True, max_length=120)
    description = serializers.CharField(required=False, max_length=240)
    expiry_date = serializers.DateField(required=False, allow_null=True)

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.expiry_date = validated_data.get("expiry_date", instance.expiry_date)

        if "label" in validated_data:
            label_guid = validated_data.pop("label")["guid"]["hex"]

            instance.label = Label.objects.get(guid=label_guid)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            instance.save()

        instance.save()
        return instance
