from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    unique_name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name