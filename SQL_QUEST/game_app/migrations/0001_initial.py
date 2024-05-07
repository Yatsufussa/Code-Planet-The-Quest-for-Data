# Generated by Django 5.0.4 on 2024-05-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cipher_Hills",
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
                ("tableid", models.IntegerField(null=True)),
                ("TableName", models.CharField(max_length=255, null=True)),
                ("RecordData_KB", models.CharField(max_length=255, null=True)),
                ("DataLoss", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Cipher_Hills2",
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
                ("tableid", models.IntegerField(null=True)),
                ("table_name", models.CharField(max_length=255, null=True)),
                ("record_data_kb", models.CharField(max_length=255, null=True)),
                ("data_loss", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DataField",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("names_of_the_hacked", models.CharField(max_length=50, null=True)),
                ("virus_name", models.CharField(max_length=50, null=True)),
                ("code_of_data", models.IntegerField(null=True)),
                ("hacking_time", models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="LakeData",
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
                ("LakeDatabase", models.CharField(max_length=50, null=True)),
                ("NumberOfAbsorbedFiles", models.IntegerField(null=True)),
                ("MainFile", models.CharField(max_length=50, null=True)),
                ("InfectionTime", models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mountain_Of_Algorithms",
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
                ("Mountain_Name", models.CharField(max_length=255, null=True)),
                ("Way_of_the_Mountain", models.CharField(max_length=255, null=True)),
                ("Path_length", models.IntegerField(null=True)),
                ("Mountain_Keeper", models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Operator_Forest",
            fields=[
                ("TrailId", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "VirusName",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("FileName", models.CharField(default=None, max_length=255, null=True)),
                ("FileWeight", models.IntegerField(default=None, null=True)),
                ("Operator", models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
    ]
