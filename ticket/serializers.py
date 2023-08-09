from rest_framework import serializers

from ticket.models import Ticket


class TicketSerializer(serializers.Serializer):
    guid = serializers.UUIDField(read_only=True, source="guid.hex")
    user_guid = serializers.CharField(required=False, source="user.guid.hex")
    label = serializers.CharField(required=True, source="label.guid.hex")
    title = serializers.CharField(required=True, max_length=120)
    description = serializers.CharField(required=True, max_length=240)
    expiry_date = serializers.DateField(required=True)

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)
