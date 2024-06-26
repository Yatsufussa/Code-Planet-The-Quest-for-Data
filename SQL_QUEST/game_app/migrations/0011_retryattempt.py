# Generated by Django 5.0.4 on 2024-05-19 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game_app", "0010_puzzletable"),
    ]

    operations = [
        migrations.CreateModel(
            name="RetryAttempt",
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
                ("retry_count", models.IntegerField(default=0)),
                (
                    "level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="game_app.level"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="game_app.player",
                    ),
                ),
            ],
        ),
    ]
