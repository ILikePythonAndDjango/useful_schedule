from django.shortcuts import render
from django.http import Http404
from django.views.decorators.http import require_GET

from .ajax import HttpResponseAjax, HttpResponseAjaxError
from .pagination import paginate_JSON

from .models import Goal, Note, Schedule

from datetime import date

@require_GET
def goals(request):
    goals = [(goal.id, goal.title, goal.url) for goal in Goal.objects.all()]
    return HttpResponseAjax(goals=goals)

def goal(request, pk):
    try:
        goal = Goal.objects.get(pk=pk)
    except Goal.DoesNotExist:
        raise Http404
    return HttpResponseAjax(
        title=goal.title,
        content=goal.content,
        deadline=str(goal.deadline),
        is_done=goal.is_done,
        cost=goal.cost,
        sub_goals=[sub_goal.title for sub_goal in goal.sub_goals.annotate()]
    )

@require_GET
def notes(request):
    notes = [(str(note.date), str(note.time)) for note in Note.objects.all()]
    return HttpResponseAjax(notes=notes)

def note(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        raise Http404
    return HttpResponseAjax(
        date=str(note.date),
        time=str(note.time),
        text=note.text,
        goals=note.goals
    )

@require_GET
def schedules(request):
    schedules = [(schedule.title, schedule.url, request.user.username) for schedule in Schedule.objects.all()]
    return HttpResponseAjax(schedules=schedules)


def schedule(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
        tasks = []
        for task in schedule.tasks.annotate():
            tasks.append(dict([
                ('title', task.title),
                ('description', task.description),
                ('begin', str(task.begin)),
                ('end', str(task.end)),
                ('time', task.time)
            ]))
    except Schedule.DoesNotExist:
        raise Http404
    return HttpResponseAjax(
        title=schedule.title,
        url=schedule.url,
        hours=schedule.hours,
        tasks=tasks
    )