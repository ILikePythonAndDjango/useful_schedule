from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User

from .ajax import HttpResponseAjax, HttpResponseAjaxError

from .models import Goal, Note, Schedule, CostControl

from datetime import date

def checking_user(view):

    """
    This function is decorator that checks user every request.
    """

    def check_user(request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseAjaxError(code=14, message="You are not authenticated!")
        else:
            return view(request, *args, **kwargs)

    return check_user

@csrf_exempt
@require_POST
def log_in(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
    except MultiValueDictKeyError:
        return HttpResponseAjaxError(code=15, message="Post params don't contain username or password!")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseAjax(message="You have logged in!")
    return HttpResponseAjaxError(code=12, message='Invalied password or username')

@csrf_exempt
@require_POST
def log_out(request):
    logout(request)
    return HttpResponseAjax(message="You have logged out!")

@csrf_exempt
@require_POST
def sign_up(request):
    try:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
    except MultiValueDictKeyError:
        return HttpResponseAjaxError(code=15, message="Post params don't contain usernam, password or email!")
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponseAjaxError(code=13, message='The user have been yet')
    user = User.objects.create_user(email=email, username=username, password=password)
    login(request, user)
    return HttpResponseAjax(message="You have signed up and logged in!")

@require_GET
@checking_user
def goals(request):
    goals = [{'id': goal.id, 'title': goal.title, 'url': goal.url} for goal in Goal.objects.filter(author=request.user)]
    return HttpResponseAjax(sequence=goals)

@checking_user
def goal(request, pk):
    try:
        goal = Goal.objects.get(pk=pk, author=request.user)
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
@checking_user
def notes(request):
    notes = [{'title': str(note.date), 'url': note.url} for note in Note.objects.filter(author=request.user)]
    return HttpResponseAjax(sequence=notes)

@checking_user
def note(request, pk):
    try:
        note = Note.objects.get(pk=pk, author=request.user)
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

@checking_user
def cost(request, pk):
    try:
        cost = CostControl.objects.get(pk=pk, author=request.user)
    except CostControl.DoesNotExist:
        raise Http404
    return HttpResponseAjax(cost={
        'thing': cost.thing,
        'cost': cost.cost
    })

@require_GET
@checking_user
def schedules(request):
    schedules = [{'title': schedule.title, 'url': schedule.url} for schedule in Schedule.objects.filter(author=request.user)]
    return HttpResponseAjax(sequence=schedules)


@checking_user
def schedule(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk, author=request.user)
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