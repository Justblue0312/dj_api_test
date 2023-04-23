from django.utils.text import slugify
from rest_framework import serializers
from .models import (
    Category,
    Product
)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(method_name='get_products')

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "slug",
            "featured",
            "products",
            "created_date",
        )

    def get_products(self, obj):
        return ProductsSerializer(obj.products.all(), many=True).data


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = {
            'id': instance.category.id,
            'slug': instance.category.slug,
            'title': instance.category.title,
        }
        return context

    def update(self, instance, validated_data):
        context = super().update(instance, validated_data)
        context.slug = slugify(instance.title)
        context.save()
        return context


class ProductSerializer(serializers.ModelSerializer):
    related_products = serializers.SerializerMethodField(
        method_name='get_related_products')

    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "title",
            "slug",
            "featured",
            "thumbnail",
            "description",
            "price",
            "created_date",
            "updated_date",
            "related_products"
        )

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = {
            'id': instance.category.id,
            'slug': instance.category.slug,
            'title': instance.category.title,
        }
        return context

    def get_related_products(self, obj):
        return ProductsSerializer(obj.related, many=True).data
