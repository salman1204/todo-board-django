from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from label.models import Label
from ticket.serializers import TicketSerializer

# Create your views here.


class TicketApiView(GenericAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

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
