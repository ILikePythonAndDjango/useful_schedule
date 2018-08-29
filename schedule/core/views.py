from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.timezone import now

from django.contrib.auth.models import User

from .ajax import HttpResponseAjax, HttpResponseAjaxError

from .models import Goal, Note, Schedule, CostControl, TypeGoal

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

@csrf_exempt
@checking_user
def goal(request, pk):

    if request.method == 'POST':

        if request.POST.get('delete_goal', False):
            try:
                Goal.objects.get(pk=pk).delete()
            except Goal.DoesNotExist:
                raise Http404
            return HttpResponseAjax(message="Goal was deleted!!!")

        try:
            #checking contains params that must contains in POST
            new_goal_title = request.POST.get('title')
            new_goal_content = request.POST.get('content')
            new_goal_deadline = request.POST.get('deadline')
        except MultiValueDictKeyError:
            return HttpResponseAjaxError(code=16, message="You've not puted params that must contians in POST")

        #params that should contains in POST
        try:
            new_goal_type_goal_id = int(request.POST.get('type_goal_id', 1))
        except ValueError:
            return HttpResponseAjaxError(code=17, message="Invalid POST params!!")
        #may be request.POST.get('begin') raise Error
        new_goal_begin = request.POST.get('begin', now())
        new_goal_is_done = bool(request.POST.get('begin', False))
        new_goal_sub_goals_id = request.POST.get('sub_goals_id', tuple())
        new_goal_cost = request.POST.get('cost', None)

        #creating new goal
        new_goal = Goal.objects.create(
            title=new_goal_title,
            content=new_goal_content,
            author=request.user,
            tag=TypeGoal.objects.get(id=new_goal_type_goal_id),
            begin=new_goal_begin,
            deadline=new_goal_deadline,
            is_done=new_goal_is_done,
            cost=new_goal_cost
        )

        if new_goal_sub_goals_id:
            #appending sub goals into new goal
            for sub_goal_id in new_goal_sub_goals_id:
                try:
                    sub_goal = Goal.objects.get(id=sub_goal_id)
                except Goal.DoesNotExist:
                    return HttpResponseAjaxError(code=18, message="This sub goal does not exits!!!")
                if sub_goal.tag__id != 2:
                    return HttpResponseAjaxError(code=19, message="This goal isn't sub goal!!")
                new_goal.sub_goals.add(sub_goal)
            new_goal.save()

        return HttpResponseAjax(message="Goal was created!!!", new_goal={
            "title": new_goal.title,
            "content": new_goal.content,
            "author_name": new_goal.author.username,
            "tag_title": new_goal.tag.title,
            "begin": str(new_goal.begin),
            "deadline": str(new_goal.deadline),
            "is_done": new_goal.is_done,
            #"sub_goals": [(sug_goal.title, sub_goal.url) for sub_goal in new_goal.sub_goals],
            "cost": new_goal.cost,
        })

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
    notes = [{'title': str(note.date), 'url': note.url} for note in Note.objects.filter(author__id=request.user.id)]
    return HttpResponseAjax(sequence=notes)

@csrf_exempt
@checking_user
def note(request, pk):

    if request.method == 'POST':

        if request.POST.get("delete_note", False):
            try:
                Note.objects.get(pk=pk).delete()
            except Note.DoesNotExist:
                raise Http404
            return HttpResponseAjax(message="Note was deleted!!!")

        try:
            #checking contains params that must contains in POST
            new_note_text = request.POST.get("text")
        except MultiValueDictKeyError:
            return HttpResponseAjaxError(code=17, message="Invalid POST params!!")

        new_note_cost_controls_id = request.POST.get('cost_controls_id', tuple())

        with open("/home/nikita/development/python3/WebDev/Django2.0.5/dev/useful_schedule/schedule/core/log.log", "w") as log:
            log.write(str(new_note_cost_controls_id))

        new_note = Note.objects.create(
            text = new_note_text,
            author = request.user
        )

        if new_note_cost_controls_id and not new_note_cost_controls_id.startswith(","):

            new_note_cost_controls_id = map(lambda x: int(x), new_note_cost_controls_id.split(","))

            #appending cost controls into new note
            for cost_control_id in new_note_cost_controls_id:
                try:
                    cost_control = CostControl.objects.get(id=cost_control_id)
                except CostControl.DoesNotExist:
                    return HttpResponseAjaxError(code=18, message="This cost contorl does not exists!!")
                new_note.cost_control.add(cost_control)
            new_note.save()

        return HttpResponseAjax(message="Note was created!!!", new_note={
            "id": new_note.id,
            "time": str(new_note.time),
            "date": str(new_note.date),
            "text": new_note.text,
            "author": new_note.author.username,
            "total_cost": new_note.total_cost
        })

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

@csrf_exempt
@checking_user
def cost(request, pk):

    if request.method == "POST":

        if request.POST.get("delete_cost", False):
            try:
                CostControl.objects.get(pk=pk).delete()
            except CostControl.DoesNotExist:
                raise Http404
            return HttpResponseAjax(message="Cost was deleted!!!")

        try:
            #checking contains params that must contains in POST
            new_cost_control_thing = request.POST.get("thing")
            new_cost_control_cost = request.POST.get('cost')
        except MultiValueDictKeyError:
            return HttpResponseAjaxError(code=17, message="Invalid POST params!!")

        #creating new cost control
        new_cost_control = CostControl.objects.create(
            thing=new_cost_control_thing,
            cost=new_cost_control_cost,
            author=request.user
        )

        return HttpResponseAjax(message='Cost Control was created', new_cost_control={
            "id": new_cost_control.id,
            "thing": new_cost_control.thing,
            "cost": new_cost_control.cost,
        })

    #initialization GET params
    try:
        is_latest_for_this_user = int(request.GET.get("new", 0))
    except ValueError:
        return HttpResponseAjaxError(code=20, message='Invalid GET params!!')


    ''' CODE BELOW IS'NT USEFUL '''
    #returns the latest cost control for this user
    if is_latest_for_this_user :
        try:
            latest_created_cost_control_for_this_user = CostControl.objects.filter(author=request.user)[0]
        except CostControl.DoesNotExist:
            return HttpResponseAjaxError(code=21, message="You don't have any cost control!!!")
        else:
            return HttpResponseAjax(latest_cost_control={
                "id": latest_created_cost_control_for_this_user.id,
                "thing": latest_created_cost_control_for_this_user.thing,
                "cost": latest_created_cost_control_for_this_user.cost,
            })            

    #returns the cost control
    try:
        cost = CostControl.objects.get(pk=pk, author=request.user)
    except CostControl.DoesNotExist:
        raise Http404
    return HttpResponseAjax(cost={
        'id': cost.id,
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
