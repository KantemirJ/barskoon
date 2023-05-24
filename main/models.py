from django.db import models


class Ad(models.Model):
    date = models.DateField()
    header = models.CharField(max_length=500)
    picture_url = models.CharField(max_length=255)
    second_picture = models.CharField(max_length=255)
    text = models.CharField(max_length=100000)


class Employee(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=10)
    job_position = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=255)
    second_picture = models.CharField(max_length=255)
    info = models.CharField(max_length=100000)


class History(models.Model):
    header = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=255)
    info = models.CharField(max_length=100000)