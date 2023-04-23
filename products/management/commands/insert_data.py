from django.core.management import BaseCommand
from django.utils.text import slugify
from products.models import (
    Category,
    Product
)
from typing import Any, Optional
import requests


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        print('Creating data...')
        response = requests.get('https://fakestoreapi.com/products').json()

        for product in response:
            category, _ = Category.objects.get_or_create(
                title=product['category'],
                slug=slugify(product['category'])
            )
            Product.objects.create(
                category=category,
                title=product['title'],
                slug=slugify(product['title']),
                price=product['price'],
                thumbnail=product['image'],
                description=product['description']
            )
        print('Completed!!!')

        # return super().handle(*args, **options)
