from django.contrib import admin
from .models import TypeGoal, Goal, Note

#Goals
admin.site.register(TypeGoal)
admin.site.register(Goal)

#Notes
admin.site.register(Note)
