from django.db import models
class TempLog(models.Model):
    val = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
class Meta:
    db_table = 'mybase'
    