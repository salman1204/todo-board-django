from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from label.serializers import LabelSerializer

# Create your views here.


class LabelApiView(GenericAPIView):
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        payload = request.data

        serializer = self.serializer_class(data=payload)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
