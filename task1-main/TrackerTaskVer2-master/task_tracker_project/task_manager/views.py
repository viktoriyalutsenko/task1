# Файл task_manager/views.py

from .models import Task
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import TaskForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Фильтрация задач по текущему пользователю
    return render(request, 'task_manager/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Присвоение текущего пользователя как владельца задачи
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_manager/task_form.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:  # Проверка, что пользователь имеет доступ к редактированию задачи
        # Вывести сообщение об ошибке или выполнить другие действия
        pass
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_manager/task_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('task_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Используем форму аутентификации
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')
            else:
                # Обработка ошибки входа
                pass
    else:
        form = AuthenticationForm()  # Создаем пустую форму для рендеринга страницы

    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_view(request):  # Представление для выхода из учетной записи
    logout(request)
    return redirect('login')