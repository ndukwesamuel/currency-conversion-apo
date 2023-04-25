# Generated by Django 4.1.7 on 2023-04-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExchangeRate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "base_currency",
                    models.CharField(
                        choices=[
                            ("USD", "US Dollar"),
                            ("GBP", "British Pound"),
                            ("NGN", "Nigerian Naira"),
                            ("EUR", "Euro"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "target_currency",
                    models.CharField(
                        choices=[
                            ("USD", "US Dollar"),
                            ("GBP", "British Pound"),
                            ("NGN", "Nigerian Naira"),
                            ("EUR", "Euro"),
                        ],
                        max_length=3,
                    ),
                ),
                ("exchange_rate", models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
