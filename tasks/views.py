from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .forms import PropietarioForm
from .forms import FamiliarDifuntoForm
from .models import Task
from .models import Propietario
from .models import FamiliarDifunto
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()   # me guarda el usuario en la BD
                login(request, user)  # me crea una cookkie con la session
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')



@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks': tasks})

# ----------------------------------- tasks--------------------------------------- 
@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()  # guarda los datos dentro de la BD
            # print(request.POST)
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Please provide valid data'
            })

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        # task = Task.objects.get(pk=task_id)
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save() # aqui actualiza mi tarea
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task'})



@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
# ----------------------------------- Propietario--------------------------------------- 
@login_required
def create_propietario(request):
    if request.method == 'GET':
        return render(request, 'create_propietario.html', {
            'form': PropietarioForm
        })
    else:
        try:
            form = PropietarioForm(request.POST)
            new_propietario = form.save(commit=False)
            new_propietario.user = request.user
            new_propietario.save()  # guarda los datos dentro de la BD
            # print(request.POST)
            return redirect('propietarios')
        except ValueError:
            return render(request, 'create_propietario.html', {
                'form': PropietarioForm,
                'error': 'Please provide valid data'
            })

@login_required
def propietarios(request):
    propietarios = Propietario.objects.filter(user=request.user)
    return render(request, 'propietarios.html', {'propietarios': propietarios})

# @login_required
# def task_detail(request, task_id):
#     if request.method == 'GET':
#         # task = Task.objects.get(pk=task_id)
#         task = get_object_or_404(Task, pk=task_id, user=request.user)
#         form = TaskForm(instance=task)
#         return render(request, 'task_detail.html', {'task': task, 'form': form})
#     else:
#         try:
#             task = get_object_or_404(Task, pk=task_id, user=request.user)
#             form = TaskForm(request.POST, instance=task)
#             form.save() # aqui actualiza mi tarea
#             return redirect('tasks')
#         except ValueError:
#             return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task'})



# @login_required
# def delete_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id, user=request.user)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('tasks')
    
# ----------------------------------- familiarDifunto--------------------------------------- 
@login_required
def create_familiarDifunto(request):
    if request.method == 'GET':
        return render(request, 'create_familiarDifunto.html', {
            'form': FamiliarDifuntoForm
        })
    else:
        try:
            form = FamiliarDifuntoForm(request.POST)
            new_familiarDifunto = form.save(commit=False)
            new_familiarDifunto.user = request.user
            new_familiarDifunto.save()  # guarda los datos dentro de la BD
            # print(request.POST)
            return redirect('familiaresDifunto')
        except ValueError:
            return render(request, 'create_familiarDifunto.html', {
                'form': FamiliarDifuntoForm,
                'error': 'Please provide valid data'
            })

@login_required
def familiaresDifunto(request):
    familiaresDifunto = FamiliarDifunto.objects.filter(user=request.user)
    return render(request, 'familiaresDifunto.html', {'familiaresDifunto': familiaresDifunto})

# @login_required
# def task_detail(request, task_id):
#     if request.method == 'GET':
#         # task = Task.objects.get(pk=task_id)
#         task = get_object_or_404(Task, pk=task_id, user=request.user)
#         form = TaskForm(instance=task)
#         return render(request, 'task_detail.html', {'task': task, 'form': form})
#     else:
#         try:
#             task = get_object_or_404(Task, pk=task_id, user=request.user)
#             form = TaskForm(request.POST, instance=task)
#             form.save() # aqui actualiza mi tarea
#             return redirect('tasks')
#         except ValueError:
#             return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task'})



# @login_required
# def delete_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id, user=request.user)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('tasks')
    
# ----------------------------------- Boveda--------------------------------------- 
# ----------------------------------- Difunto--------------------------------------- 

@login_required
def signout(request):
    logout(request)  # me borra la cookie de la sessionId
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        # authenticate sirve para autenticar que el usuario y pass ingresados correspondan con alguno en la BD
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or passsword is incorrect'
            })
        else:
            login(request, user)  # guarda la session en una cookie
            return redirect('tasks')
