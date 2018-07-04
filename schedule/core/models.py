from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

class TypeGoal(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Goal(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(
        TypeGoal, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    begin = models.DateField(default=now().date())
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)
    sub_goals = models.ManyToManyField('Goal', blank=True)
    cost = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def url(self):
        '''Gets current url for the goal.'''
        return reverse('goal', kwargs={'pk': self.id})

    @property
    def time(self):
        '''returns the difference between the beginning of the goal and its deadline'''
        return self.deadline - self.begin

class Note(models.Model):
    
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)
    goals = models.ForeignKey(
        Goal, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return 'Day: {}, time: {}'.format(self.date, self.time)