from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    uid = models.CharField(max_length=32, unique=True)
    wtoken = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        unique_together = ('name', 'pwd')