# Generated by Django 4.1.5 on 2023-01-26 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["title"], "verbose_name": "Categorie"},
        ),
    ]
