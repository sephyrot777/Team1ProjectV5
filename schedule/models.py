from django.db import models

# Create your models here.

class Schedule(models.Model):
    id = models.AutoField(primary_key = True)
    date = models.TextField()
    time = models.TextField()
    home = models.TextField()
    score = models.TextField()
    away = models.TextField()


    class Meta:
        db_table = 'schedule'
