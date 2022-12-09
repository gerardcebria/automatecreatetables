from django.db import models

# Create your models here.

class DataBaseProject(models.Model):

    server = models.CharField(max_length=255)
    database = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)

    def __str__(self):
        return self.name