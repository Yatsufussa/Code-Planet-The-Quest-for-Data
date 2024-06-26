# Generated by Django 5.0.4 on 2024-05-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
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
                ("nickname", models.CharField(max_length=255, null=True)),
                (
                    "registration_time",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("p_level", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
