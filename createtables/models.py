from django.db import models

# Create your models here.

class DataBaseProject(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    database = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name