from django.db import models
from django.db.models import CharField, Model


# Create your models here.
class UrlAlias(models.Model):
    alias = models.CharField(max_length=8, unique=True)
    url = models.TextField()

    def __str__(self):
        return self.alias