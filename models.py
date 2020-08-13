from django.db import models


class Members(models.Model):
    id = models.CharField(max_length=200)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)


class Activity(models.Model):
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)










# Create your models here.
