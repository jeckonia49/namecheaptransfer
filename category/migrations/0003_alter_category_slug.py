# Generated by Django 4.2.4 on 2023-08-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0002_category_slug_alter_category_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]