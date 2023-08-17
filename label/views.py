from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from label.models import Label
from label.serializers import LabelSerializer

# Create your views here.


class LabelApiView(GenericAPIView):
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user_all_labels = Label.objects.filter(user=request.user).all()

            serializer = self.serializer_class(user_all_labels, many=True)

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

        serializer = self.serializer_class(data=payload)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelDetailsApiView(GenericAPIView):
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, label_guid):
        payload = request.data

        label_instance = Label.objects.filter(
            user=request.user, guid=label_guid
        ).last()

        if not label_instance:
            return Response(
                data={"detail": "Label not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(label_instance, data=payload, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, label_guid):
        label_instance = Label.objects.filter(
            user=request.user, guid=label_guid
        ).last()

        if not label_instance:
            return Response(
                data={"detail": "Label not found"}, status=status.HTTP_404_NOT_FOUND
            )

        label_instance.delete()

        return Response(
            {
                "data": {},
                "response_message": "Label have been deleted successfully.",
                "response_code": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,)
