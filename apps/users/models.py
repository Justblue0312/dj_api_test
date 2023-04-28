from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser, update_last_login
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_bytes
from django.contrib.auth.tokens import default_token_generator
from uuid import uuid4
from .validators import name_validator


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid4,
        unique=True,
        auto_created=True,
        editable=False,
        blank=False,
        primary_key=True,
    )
    username = models.CharField(max_length=50, unique=True, validators=[name_validator])
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    USERNAME_FIELD = "username"

    class Meta:
        db_table = "users"
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.get_full_name().title()

    @property
    def get_full_name(self) -> str:
        return super().get_full_name()

    @staticmethod
    def get_user_from_uuid(uuid):
        uid = urlsafe_base64_decode(uuid).decode()
        user = get_object_or_404(User, id=uid)
        return user

    def check_password(self, raw_password: str) -> bool:
        if not super().check_password(raw_password):
            raise ValidationError("user password is incorrect")
        return True

    def generate_uuid(self):
        uidb64 = urlsafe_base64_encode(smart_bytes(self.id))
        return uidb64

    def generate_token(self):
        token = default_token_generator.make_token(self)
        return token

    def check_token_validation(self, token):
        if not default_token_generator.check_token(self, token):
            raise ValidationError("token is invalid or expired")

    def update_login(self):
        update_last_login(User, user=self)
