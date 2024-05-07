from django.db import models


class DataField(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically incrementing unique ID
    names_of_the_hacked = models.CharField(max_length=50, null=True)
    virus_name = models.CharField(max_length=50, null=True)
    code_of_data = models.IntegerField(null=True)
    hacking_time = models.TimeField(null=True)


class LakeData(models.Model):
    LakeDatabase = models.CharField(max_length=50, null=True)
    NumberOfAbsorbedFiles = models.IntegerField(null=True)
    MainFile = models.CharField(max_length=50, null=True)
    InfectionTime = models.TimeField(null=True)


class Mountain_Of_Algorithms(models.Model):
    Mountain_Name = models.CharField(max_length=255, null=True)
    Way_of_the_Mountain = models.CharField(max_length=255, null=True)
    Path_length = models.IntegerField(null=True)
    Mountain_Keeper = models.CharField(max_length=255, null=True)


class Operator_Forest(models.Model):
    TrailId = models.IntegerField(primary_key=True)
    VirusName = models.CharField(max_length=255, null=True, default=None)
    FileName = models.CharField(max_length=255, null=True, default=None)
    FileWeight = models.IntegerField(null=True, default=None)
    Operator = models.CharField(max_length=255, null=True, default=None)


#lvl 6-1
class Cipher_Hills(models.Model):
    tableid = models.IntegerField(null=True)
    TableName = models.CharField(max_length=255, null=True)
    RecordData_KB = models.CharField(max_length=255, null=True)
    DataLoss = models.IntegerField(null=True)

    #lvl6-2


class Cipher_Hills2(models.Model):
    table_id = models.IntegerField(null=True)
    table_name = models.CharField(max_length=255, null=True)
    record_data_kb = models.CharField(max_length=255, null=True)
    data_loss = models.IntegerField(null=True)
