# Generated by Django 4.2.3 on 2023-07-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chryblk", "0002_quandldata"),
    ]

    operations = [
        migrations.AddField(
            model_name="quandldata",
            name="average",
            field=models.FloatField(default=0.0),
        ),
    ]
