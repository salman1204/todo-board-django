from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user.serializers import UserSignupSerializer


# Create your views here.


class UserSignupView(GenericAPIView):
    serializer_class = UserSignupSerializer

    def post(self, request):
        payload = request.data

        serializer = self.serializer_class(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
