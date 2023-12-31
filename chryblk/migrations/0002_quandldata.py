# Generated by Django 4.2.3 on 2023-07-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chryblk", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuandlData",
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
                ("ticker", models.CharField(max_length=10)),
                ("date", models.DateField()),
                ("open_price", models.FloatField()),
                ("high", models.FloatField()),
                ("low", models.FloatField()),
                ("close", models.FloatField()),
                ("volume", models.IntegerField()),
                ("change", models.FloatField()),
            ],
        ),
    ]
