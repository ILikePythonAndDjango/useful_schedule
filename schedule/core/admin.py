from django.contrib import admin
from .models import TypeGoal, Goal, Note, Schedule, Task

#Goals
admin.site.register(TypeGoal)
admin.site.register(Goal)

#Notes
admin.site.register(Note)

#Schedule
admin.site.register(Task)
admin.site.register(Schedule)