from django.db import models
from django.contrib.auth.models import User

class TypeGoal(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Goal(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(TypeGoal, on_delete=models.SET_NULL, blank=True, null=True)
    begin = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)
    sub_goals = models.ManyToManyField('Goal', blank=True)
    cost = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
