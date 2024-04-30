from django.db import models

class NewModel(models.Model):
    username = models.CharField(max_length=290)
    age = models.IntegerField()
    email = models.CharField(max_length=290)
    password = models.CharField(max_length=255)
   
