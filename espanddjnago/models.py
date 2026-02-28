from django.db import models

# Create your models here.
class TempLog(models.Model):
    val = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    