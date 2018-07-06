from django.contrib import admin
from .models import TypeGoal, Goal, Note, Schedule, Task, CostControl

#Goals
admin.site.register(TypeGoal)
admin.site.register(Goal)

#Notes
admin.site.register(Note)
admin.site.register(CostControl)

#Schedule
admin.site.register(Task)
admin.site.register(Schedule)