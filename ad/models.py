from django.db import models
from main.models import Ad
from django.contrib.auth.models import User


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Ad, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
