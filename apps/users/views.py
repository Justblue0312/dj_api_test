from rest_framework import generics, permissions
from .serializer import UsersSerializer, UserSerializer
from .models import User


class ListUser(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UsersSerializer

    def get_queryset(self):
        return User.objects.order_by("-created_at").filter(is_superuser=False)


class RetriveUser(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"


class CreateUser(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class UpdateUser(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser,
    ]
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class DeleteUser(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    queryset = User.objects.all()
    serializer_class = UsersSerializer
