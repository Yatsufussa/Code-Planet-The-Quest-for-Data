# game_app/migrations/0002_setup_performance_criteria.py
from django.db import migrations
from datetime import timedelta


def setup_performance_criteria(apps, schema_editor):
    Level = apps.get_model('game_app', 'Level')
    Performance = apps.get_model('game_app', 'Performance')

    level1, created = Level.objects.get_or_create(id=1, defaults={'title': 'Level 1'})
    Performance.objects.update_or_create(
        level=level1,
        defaults={
            'top_time': timedelta(minutes=5),
            'medium_time': timedelta(minutes=10),
            'bad_time': timedelta(minutes=15)
        }
    )


class Migration(migrations.Migration):
    dependencies = [
        ('game_app', '0001_initial'),  # Adjust the dependency as necessary
    ]

    operations = [
        migrations.RunPython(setup_performance_criteria),
    ]
