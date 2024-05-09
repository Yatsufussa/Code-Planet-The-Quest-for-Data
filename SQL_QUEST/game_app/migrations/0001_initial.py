# Generated by Django 5.0.4 on 2024-05-09 19:04

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
                ("EncryptionID", models.IntegerField(default=None, null=True)),
                (
                    "CoderName",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("KeyBit", models.IntegerField(default=None, null=True)),
                ("Operator", models.CharField(default=None, max_length=255, null=True)),
                (
                    "VirusFound",
                    models.CharField(default=None, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DataField",
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
                ("NamesOfTheHacked", models.CharField(max_length=50, null=True)),
                ("VirusName", models.CharField(max_length=50, null=True)),
                ("CodeOfData", models.IntegerField(null=True)),
                ("HackingTime", models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Index_Valley",
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
                    "TheDataBase",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                (
                    "IndexType",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("MainFile", models.CharField(default=None, max_length=255, null=True)),
                (
                    "FileContents",
                    models.CharField(default=None, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Index_Valley2",
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
                    "TheDataBase",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                (
                    "IndexType",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("MainFile", models.CharField(default=None, max_length=255, null=True)),
                (
                    "FileContents",
                    models.CharField(default=None, max_length=255, null=True),
                ),
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
            name="Lunar_Landscape",
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
                    "NumOfVirusLegion",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("NumOfDefeatedMinions", models.IntegerField(default=None, null=True)),
                (
                    "AccessKeyValue",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                (
                    "ReleasedFiles",
                    models.CharField(default=None, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lunar_Landscape2",
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
                    "NumOfVirusLegion",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("NumOfDefeatedMinions", models.IntegerField(default=None, null=True)),
                (
                    "AccessKeyValue",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                (
                    "ReleasedFiles",
                    models.CharField(default=None, max_length=255, null=True),
                ),
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
                ("MountainName", models.CharField(max_length=255, null=True)),
                ("WayOfTheMountain", models.CharField(max_length=255, null=True)),
                ("PathLength", models.IntegerField(null=True)),
                ("MountainKeeper", models.CharField(max_length=255, null=True)),
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
        migrations.CreateModel(
            name="Optimization_Plateau",
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
                    "IndexType",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("DataSize", models.IntegerField(default=None, null=True)),
                ("ContaminatedDataKB", models.IntegerField(default=None, null=True)),
                (
                    "Operators",
                    models.CharField(default=None, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Optimization_Plateau2",
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
                    "IndexType",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("DataSize", models.IntegerField(default=None, null=True)),
                ("ContaminatedDataKB", models.IntegerField(default=None, null=True)),
                (
                    "Operators",
                    models.CharField(default=None, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PetaByte_Bay",
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
                ("TableId", models.IntegerField(null=True)),
                ("TableName", models.CharField(max_length=255, null=True)),
                ("RecordDataKB", models.CharField(max_length=255, null=True)),
                ("DataLoss", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PetaByte_Bay2",
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
                ("TableId", models.IntegerField(null=True)),
                ("TableName", models.CharField(max_length=255, null=True)),
                ("RecordDataKB", models.CharField(max_length=255, null=True)),
                ("DataLoss", models.IntegerField(null=True)),
            ],
        ),
    ]
