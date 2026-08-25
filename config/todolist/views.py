from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm, Create_todo, LoginForm
from .models import todo_items


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('home')
    else:
        form = SignUpForm()
    # Was rendering '/registration/signup.html' (a path that doesn't exist
    # in this app and starts with a stray leading slash).
    return render(request, 'todo/signup.html', {'form': form})


def login_view(request):
    # urls.py imported a `login` view from this module that was never
    # defined here (it was accidentally shadowing django.contrib.auth.login).
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
    else:
        form = LoginForm(request)
    return render(request, 'todo/login.html', {'form': form})


@login_required
def home(request):
    tasks = request.user.tasks.all()
    return render(request, 'todo/home.html', {'tasks': tasks})


@login_required
def upload_tasks(request):
    if request.method == 'POST':
        form = Create_todo(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, 'Task uploaded!')
            return redirect('home')
    else:
        form = Create_todo()
    # Was rendering 'player/upload.html', a template from a different
    # (music player) app that doesn't exist here.
    return render(request, 'todo/upload.html', {'form': form})


@login_required
@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(todo_items, pk=pk, owner=request.user)
    task.done = not task.done
    task.save()
    return redirect('home')


@login_required
@require_POST
def delete_task(request, pk):
    task = get_object_or_404(todo_items, pk=pk, owner=request.user)
    task.delete()
    messages.success(request, 'Task deleted.')
    return redirect('home')

# upload_track / TrackUploadForm removed: they referenced a form and model
# that don't exist anywhere in this app (leftover from a different project,
# e.g. an audio player app). They would have raised NameError on every
# request the moment this URL was hit.
