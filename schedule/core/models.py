from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

class TypeGoal(models.Model):

    '''
    This model helps the application to sort goals on MainGoal and SubGoal
    '''

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Goal(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(
        'TypeGoal', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    begin = models.DateField(default=now())
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
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goals = models.ForeignKey(
        'Goal', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return 'Day: {}, time: {}'.format(self.date, self.time)

    @property
    def url(self):
        '''Gets current url for the goal.'''
        return reverse('note', kwargs={'pk': self.id})

    class Meta:
        ordering = ('-date', 'time')

class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    begin = models.TimeField(default=now())
    end = models.TimeField(default=now())

    def __str__(self):
        return self.title

    @property
    def time(self):
        return self.end - self.begin

    class Meta:
        #It's very important point, because it set order of view tasks
        ordering = ('begin',)

class Schedule(models.Model):

    title = models.CharField(max_length=100)
    tasks = models.ManyToManyField('Task', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    @property
    def hours(self):
        return sum([task.time.hour for task in self.tasks.annotate()])