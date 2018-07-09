from django.shortcuts import render
from django.http import Http404
from django.views.decorators.http import require_GET

from .ajax import HttpResponseAjax, HttpResponseAjaxError
from .pagination import paginate_JSON

from .models import Goal, Note, Schedule, CostControl

from datetime import date

@require_GET
def goals(request):
    goals = [{'title': goal.title, 'url': goal.url} for goal in Goal.objects.all()]
    return HttpResponseAjax(sequence=goals)

def goal(request, pk):
    try:
        goal = Goal.objects.get(pk=pk)
        sub_goals = [{'title': sub_goal.title, 'url': sub_goal.url} for sub_goal in goal.sub_goals.annotate()]
    except Goal.DoesNotExist:
        raise Http404
    return HttpResponseAjax(goal={
        'title': goal.title,
        'content': goal.content,
        'deadline': str(goal.deadline),
        'is_done': goal.is_done,
        'cost': goal.cost,
        'sub_goals': sub_goals
    })

@require_GET
def notes(request):
    notes = [{'title': str(note.date), 'url': note.url} for note in Note.objects.all()]
    return HttpResponseAjax(sequence=notes)

def note(request, pk):
    try:
        note = Note.objects.get(id=pk)
        cost_controls = [{'thing': cost.thing, 'url': cost.url, 'cost': cost.cost} for cost in note.cost_control.annotate()]
    except Note.DoesNotExist:
        raise Http404
    return HttpResponseAjax(note={
        'date': str(note.date),
        'time': str(note.time),
        'text': note.text,
        'cost_control': cost_controls,
        'total_cost': note.total_cost
    })

def cost(request, cost_pk):
    try:
        cost = CostControl.objects.get(id=cost_pk)
    except CostControl.DoesNotExist:
        raise Http404
    return HttpResponseAjax(cost={
        'thing': cost.thing,
        'cost': cost.cost
    })

@require_GET
def schedules(request):
    schedules = [{'title': schedule.title, 'url': schedule.url} for schedule in Schedule.objects.all()]
    return HttpResponseAjax(sequence=schedules)


def schedule(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
        tasks = []
        for task in schedule.tasks.annotate():
            tasks.append({
                'title': task.title,
                'description': task.description,
                'begin': str(task.begin),
                'end': str(task.end),
                'time': task.time
            })
    except Schedule.DoesNotExist:
        raise Http404
    return HttpResponseAjax(schedule={
        "title": schedule.title,
        "url": schedule.url,
        "hours": schedule.hours,
        "tasks": tasks
    })