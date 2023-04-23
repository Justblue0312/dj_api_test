from django.contrib import admin
from .models import (
    Category,
    Product
)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Category)
admin.site.register(Product)
