from django.db import models


class DataField(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically incrementing unique ID
    names_of_the_hacked = models.CharField(max_length=50, null=True)
    virus_name = models.CharField(max_length=50, null=True)
    code_of_data = models.IntegerField(null=True)
    hacking_time = models.TimeField(null=True)
