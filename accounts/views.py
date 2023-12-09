from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import (
    UserInformationSerializer,
    SignUpSerializer,
    User,
    EmailCheckSerializer,
)


class SignUpViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailCheckView(ViewSet):
    queryset = User.objects.all()
    serializer_class = EmailCheckSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = EmailCheckSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            if User.objects.filter(email=email).exists():
                return Response(
                    {"message": "이미 존재하는 이메일입니다."}, status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return Response(
                    {"message": "사용 가능한 이메일입니다."}, status=status.HTTP_200_OK
                )


class UserInformationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInformationSerializer
    permission_classes = [IsAuthenticated]
