from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSignupSerializer

# Create your views here.


class UserSignupView(GenericAPIView):
    serializer_class = UserSignupSerializer

    def post(self, request):
        payload = request.data

        new_user_email = payload["email"]

        is_user_exists = User.objects.filter(email=new_user_email).exists()

        if is_user_exists:
            return Response(
                {
                    "data": {},
                    "response_message": "User with this email already exists",
                    "response_code": status.HTTP_409_CONFLICT,
                },
                status=status.HTTP_409_CONFLICT,
            )

        serializer = self.serializer_class(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "data": {},
                    "response_message": "Account created successfully",
                    "response_code": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
