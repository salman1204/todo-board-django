from datetime import datetime

import rest_framework
from django.shortcuts import render
from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from label.models import Label
from ticket.models import Ticket
from ticket.serializers import TicketSerializer

# Create your views here.


class TicketApiView(GenericAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            label_guid = request.query_params.get("label")

            ticket_by_labels = Ticket.objects.filter(
                user=request.user, label__guid=label_guid
            ).all()

            serializer = self.serializer_class(ticket_by_labels, many=True)

            return Response(
                {
                    "data": serializer.data,
                    "response_message": "success",
                    "response_code": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "data": {},
                    "response_message": e.args[0],
                    "response_code": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request):
        payload = request.data

        label_instance = Label.objects.filter(
            user=request.user, guid=payload["label"]
        ).last()

        serializer = self.serializer_class(data=payload)

        if serializer.is_valid():
            serializer.save(user=request.user, label=label_instance)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailsApiView(GenericAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, ticket_guid):
        payload = request.data

        ticket_instance = Ticket.objects.filter(
            user=request.user, guid=ticket_guid
        ).last()

        if not ticket_instance:
            return Response(
                data={"detail": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(ticket_instance, data=payload, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketExpireToday(GenericAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        current_date = timezone.localtime(timezone.now()).date()
        ticket_instances = Ticket.objects.filter(
            user=request.user, expiry_date=current_date
        )

        serializer = self.serializer_class(ticket_instances, many=True)

        response_data = {
            "data": serializer.data,
            "response_message": "success",
            "response_code": status.HTTP_200_OK,
        }

        return Response(response_data, status=status.HTTP_200_OK)
