from django.db import models
from main.models import Employee
from django.contrib.auth.models import User


class CommentPerson(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
