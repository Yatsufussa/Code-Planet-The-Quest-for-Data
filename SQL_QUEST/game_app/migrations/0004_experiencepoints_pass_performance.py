# Generated by Django 5.0.4 on 2024-05-15 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game_app", "0003_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExperiencePoints",
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
                ("points", models.IntegerField()),
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
        migrations.CreateModel(
            name="Pass",
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
                ("stars", models.IntegerField(default=0)),
                ("time", models.DurationField(blank=True, null=True)),
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
        migrations.CreateModel(
            name="Performance",
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
                ("top_time", models.DurationField()),
                ("medium_time", models.DurationField()),
                ("bad_time", models.DurationField()),
                (
                    "level",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="game_app.level"
                    ),
                ),
            ],
        ),
    ]
