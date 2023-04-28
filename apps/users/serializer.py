from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = (
            "is_superuser",
            "is_staff",
            "user_permissions",
            "groups",
            "last_login",
            "date_joined",
            "is_active",
        )

    def update(self, instance, validated_data):
        context = super().update(instance, validated_data)
        context["updated_at"] = True
        context.update_login()
        context.save()
        return context


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = (
            "is_superuser",
            "is_staff",
            "user_permissions",
            "groups",
            "last_login",
            "date_joined",
            "is_active",
        )
