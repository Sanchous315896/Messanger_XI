import datetime
from http.client import HTTPResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import AUTHUserForm, REGUserForm, UpdateForm
from .models import Post, Profile


def reg(request):
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #
    #     print(form.data.get("username"))
    #     print(form.data.get("password"))

    form = REGUserForm(request.POST)
    auth_form = AUTHUserForm(request.POST)
    context = {'form': form, 'auth': auth_form}

    return render(request, 'registraiton.html', context)


def registrate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save
        login(request, user)
        return redirect('/')  # Перенаправляем пользователя на страницу входа после успешной регистрации
    # redirect("reg/")
    return redirect("reg/")


def auth(request):
    if request.method == 'POST':
        form = AUTHUserForm(request.POST)

        print(form.data.get("username"))
        print(form.data.get("password"))

    form = AUTHUserForm(request.POST)
    context = {'form': form}
    return render(request, 'authorization.html')


def authorize(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')

    return redirect("reg/")


@login_required
def logout_view(request):
    logout(request)
    return redirect('reg/')


# Илюха сюда


@login_required
def profile(request, pk):
    profile_data = Profile.objects.get(id=pk)
    user = request.user
    context = {"profile": profile_data, "user": user}
    return render(request, 'profile.html', context)


@login_required
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = UpdateForm(instance=post)

    return render(request, 'update.html', {'form': form, 'post': post})


@login_required
def update(request, pk):
    post = Post.objects.get(id=pk)
    form = UpdateForm(instance=post)

    return render(request, 'create.html', {'form': form, 'post': post})


@login_required
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    if user == post.owner:

        if request.method == 'POST':
            form = UpdateForm(request.POST or None, instance=post)
            if form.is_valid():
                post.posted_time = datetime.datetime.now()
                post.save()
                form.save()
            return redirect("/")

    else:
        form = UpdateForm(instance=post)
    return render(request, '/update/' + pk, {'form': form})


@login_required
def create(request):
    post = Post()
    form = UpdateForm(instance=post)

    return render(request, 'create.html', {'form': form})


@login_required
def create_post(request):
    post = Post()
    form = UpdateForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.owner = str(request.user)
        post.save()
        print("Created TODO")
    return redirect('/')
