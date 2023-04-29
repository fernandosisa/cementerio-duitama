from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .forms import FamiliarDifuntoForm
from .forms import PropietarioForm
from .forms import BovedaForm
from .forms import DifuntoForm
from .models import Task
from .models import FamiliarDifunto
from .models import Propietario
from .models import Boveda
from .models import Difunto
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
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
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
            form.save()  # aqui actualiza mi tarea
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


@login_required
def propietario_detail(request, propietario_id):
    if request.method == 'GET':
        # propietario = propietario.objects.get(pk=propietario_id)
        propietario = get_object_or_404(
            Propietario, pk=propietario_id, user=request.user)
        form = PropietarioForm(instance=propietario)
        return render(request, 'propietario_detail.html', {'propietario': propietario, 'form': form})
    else:
        try:
            propietario = get_object_or_404(
                Propietario, pk=propietario_id, user=request.user)
            form = PropietarioForm(request.POST, instance=propietario)
            form.save()  # aqui actualiza mi tarea
            return redirect('propietarios')
        except ValueError:
            return render(request, 'propietario_detail.html', {'propietario': propietario, 'form': form, 'error': 'Error updating propietario'})


@login_required
def delete_propietario(request, propietario_id):
    propietario = get_object_or_404(
        Propietario, pk=propietario_id, user=request.user)
    if request.method == 'POST':
        propietario.delete()
        return redirect('propietarios')

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


@login_required
def familiarDifunto_detail(request, familiarDifunto_id):
    if request.method == 'GET':
        # familiarDifunto = familiarDifunto.objects.get(pk=familiarDifunto_id)
        familiarDifunto = get_object_or_404(
            FamiliarDifunto, pk=familiarDifunto_id, user=request.user)
        form = FamiliarDifuntoForm(instance=familiarDifunto)
        return render(request, 'familiarDifunto_detail.html', {'familiarDifunto': familiarDifunto, 'form': form})
    else:
        try:
            familiarDifunto = get_object_or_404(
                FamiliarDifunto, pk=familiarDifunto_id, user=request.user)
            form = FamiliarDifuntoForm(request.POST, instance=familiarDifunto)
            form.save()  # aqui actualiza mi tarea
            return redirect('familiaresDifunto')
        except ValueError:
            return render(request, 'familiarDifunto_detail.html', {'familiarDifunto': familiarDifunto, 'form': form, 'error': 'Error updating familiarDifunto'})


@login_required
def delete_familiarDifunto(request, familiarDifunto_id):
    familiarDifunto = get_object_or_404(
        FamiliarDifunto, pk=familiarDifunto_id, user=request.user)
    if request.method == 'POST':
        familiarDifunto.delete()
        return redirect('familiaresDifunto')

# ----------------------------------- Boveda---------------------------------------

@login_required
def create_boveda(request):
    if request.method == 'GET':
        return render(request, 'create_boveda.html', {
            'form': BovedaForm
        })
    else:
        try:
            form = BovedaForm(request.POST)
            new_boveda = form.save(commit=False)
            new_boveda.user = request.user
            new_boveda.save()  # guarda los datos dentro de la BD
            # print(request.POST)
            return redirect('bovedas')
        except ValueError:
            return render(request, 'create_boveda.html', {
                'form': BovedaForm,
                'error': 'Please provide valid data'
            })


@login_required
def bovedas(request):
    bovedas = Boveda.objects.filter(user=request.user)
    return render(request, 'bovedas.html', {'bovedas': bovedas})


@login_required
def boveda_detail(request, boveda_id):
    if request.method == 'GET':
        # boveda = boveda.objects.get(pk=boveda_id)
        boveda = get_object_or_404(
            Boveda, pk=boveda_id, user=request.user)
        form = BovedaForm(instance=boveda)
        return render(request, 'boveda_detail.html', {'boveda': boveda, 'form': form})
    else:
        try:
            boveda = get_object_or_404(
                Boveda, pk=boveda_id, user=request.user)
            form = BovedaForm(request.POST, instance=boveda)
            form.save()  # aqui actualiza mi tarea
            return redirect('bovedas')
        except ValueError:
            return render(request, 'boveda_detail.html', {'boveda': boveda, 'form': form, 'error': 'Error updating boveda'})


@login_required
def delete_boveda(request, boveda_id):
    boveda = get_object_or_404(
        Boveda, pk=boveda_id, user=request.user)
    if request.method == 'POST':
        boveda.delete()
        return redirect('bovedas')

# ----------------------------------- Difunto---------------------------------------

@login_required
def create_difunto(request):
    if request.method == 'GET':
        return render(request, 'create_difunto.html', {
            'form': DifuntoForm
        })
    else:
        try:
            form = DifuntoForm(request.POST)
            new_difunto = form.save(commit=False)
            new_difunto.user = request.user
            new_difunto.save()  # guarda los datos dentro de la BD
            # print(request.POST)
            return redirect('difuntos')
        except ValueError:
            return render(request, 'create_difunto.html', {
                'form': DifuntoForm,
                'error': 'Please provide valid data'
            })



@login_required
def difunto_detail(request, difunto_id):
    if request.method == 'GET':
        # difunto = difunto.objects.get(pk=difunto_id)
        difunto = get_object_or_404(
            Difunto, pk=difunto_id, user=request.user)
        form = DifuntoForm(instance=difunto)
        return render(request, 'difunto_detail.html', {'difunto': difunto, 'form': form})
    else:
        try:
            difunto = get_object_or_404(
                Difunto, pk=difunto_id, user=request.user)
            form = DifuntoForm(request.POST, instance=difunto)
            form.save()  # aqui actualiza mi tarea
            return redirect('difuntos')
        except ValueError:
            return render(request, 'difunto_detail.html', {'difunto': difunto, 'form': form, 'error': 'Error updating difunto'})


@login_required
def delete_difunto(request, difunto_id):
    difunto = get_object_or_404(
        Difunto, pk=difunto_id, user=request.user)
    if request.method == 'POST':
        difunto.delete()
        return redirect('difuntos')


# ----------------------------termina difunto------------------

@login_required
def difuntos(request):
    difuntos = Difunto.objects.filter(user=request.user)
    return render(request, 'difuntos.html', {'difuntos': difuntos})

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
