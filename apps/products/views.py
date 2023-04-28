from rest_framework import generics
from rest_framework import permissions
from .models import Category, Product
from .serializers import (
    ProductsSerializer,
    CategoriesSerializer,
    ProductSerializer,
    CategorySerializer,
)


class ListProduct(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    # queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Product.objects.order_by("-id")


class ListCategory(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class RetriveProduct(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"


class RetriveCategory(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"


class CreateProduct(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class UpdateProduct(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class DestroyProduct(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
