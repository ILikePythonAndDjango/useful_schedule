from django.db import models
from django.contrib.auth.models import User

class TypeGoal(models.Model):

    title = models.CharField(max_length)

class Goal(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User)
    tag = models.ForeignKey(TypeGoal)
    begin = 
