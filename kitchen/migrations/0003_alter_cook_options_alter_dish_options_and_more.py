# Generated by Django 4.1.7 on 2023-03-30 16:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={
                "ordering": ["username"],
                "verbose_name": "cook",
                "verbose_name_plural": "cooks",
            },
        ),
        migrations.AlterModelOptions(
            name="dish",
            options={
                "ordering": ["name"],
                "verbose_name": "dish",
                "verbose_name_plural": "dishes",
            },
        ),
        migrations.AlterField(
            model_name="dish",
            name="cooks",
            field=models.ManyToManyField(
                blank=True, related_name="dishes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
