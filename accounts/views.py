from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import logging

logger = logging.getLogger(__name__)


class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)

        except Exception:
            logger.exception("REGISTER API ERROR")
            raise


class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "mrssage": "You are authenticated",
            "useraname": request.user.username,
            "email": request.user.email
        })