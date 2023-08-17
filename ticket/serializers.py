import datetime

from rest_framework import serializers

from label.models import Label
from ticket.models import Ticket, TicketHistory


class TicketSerializer(serializers.Serializer):
    guid = serializers.UUIDField(read_only=True, source="guid.hex")
    user_guid = serializers.CharField(required=False, source="user.guid.hex")
    label = serializers.CharField(required=True, source="label.guid.hex")
    label_title = serializers.CharField(required=False, source="label.title")
    title = serializers.CharField(required=True, max_length=120)
    description = serializers.CharField(required=False, max_length=240, allow_null=True)
    expiry_date = serializers.DateField(
        required=False, allow_null=True, format="%d-%m-%Y", input_formats=["%d-%m-%Y"]
    )

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.expiry_date = validated_data.get("expiry_date", instance.expiry_date)

        if "label" in validated_data:
            label_guid = validated_data.pop("label")["guid"]["hex"]
            instance.label = Label.objects.get(guid=label_guid)

            TicketHistory.objects.create(
                user=instance.user,
                label=instance.label,
                ticket=instance,
                time=datetime.datetime.now()  # You can customize the time value here
            )

            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            instance.save()

        instance.save()
        return instance


class TicketHistorySerializer(serializers.Serializer):
    guid = serializers.UUIDField(read_only=True, source="guid.hex")
    label_title = serializers.CharField(required=False, source="label.title")
    ticket_title = serializers.CharField(required=False, source="ticket.title")
    time = serializers.DateTimeField(
        required=False, allow_null=True, format="%d-%m-%Y %H:%M:%S", input_formats=["%d-%m-%Y %H:%M:%S"]
    )

    def create(self, validated_data):
        return TicketHistory.objects.create(**validated_data)
