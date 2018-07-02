from django.shortcuts import render

from .ajax import HttpResponseAjax, HttpResponseAjaxError

from .models import Goal

def goals(request):
	goals = [goal.title for goal in Goal.objects.all()[:]]
	return HttpResponseAjax(goals=goals)