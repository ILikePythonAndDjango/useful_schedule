from django.shortcuts import render

from .ajax import HttpResponseAjax, HttpResponseAjaxError

from .models import Goal

def goals(request):
    goals = [(goal.title, goal.url) for goal in Goal.objects.all()[:]]
    return HttpResponseAjax(goals=goals)

def goal(request, pk):
    g = Goal.objects.get(pk=pk)
    return HttpResponseAjax(
        tittle=g.title,
        content=g.content,
        deadline=g.deadline,
        is_done=g.is_done,
        cost=g.cost
    )