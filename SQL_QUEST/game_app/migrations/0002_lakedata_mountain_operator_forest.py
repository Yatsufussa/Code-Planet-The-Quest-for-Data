# Generated by Django 5.0.4 on 2024-04-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LakeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LakeDatabase', models.CharField(max_length=50, null=True)),
                ('NumberOfAbsorbedFiles', models.IntegerField(null=True)),
                ('MainFile', models.CharField(max_length=50, null=True)),
                ('DamageToTheLake_Percent', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('InfectionTime', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MountainName', models.CharField(max_length=255, null=True)),
                ('TheWayofTheMountain', models.CharField(max_length=255, null=True)),
                ('Pathlength', models.IntegerField(null=True)),
                ('KeeperoftheMountain', models.CharField(max_length=255, null=True)),
                ('AchanceToPassTheMountain', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operator_Forest',
            fields=[
                ('TrailId', models.IntegerField(primary_key=True, serialize=False)),
                ('VirusName', models.CharField(default=None, max_length=255, null=True)),
                ('FileName', models.CharField(default=None, max_length=255, null=True)),
                ('FileWeight', models.IntegerField(default=None, null=True)),
                ('Operator', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
    ]