from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.form import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            context = {'errors': form.errors}
            return render(request, 'user/register.html', context)

    else:
        return render(request, 'user/register.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                context = {'error': 'Username or password is incorrect.'}
                return render(request, 'user/login.html', context)

        else:
            context = {'errors': form.errors}
            return render(request, 'user/login.html', context)

    else:
        return render(request, 'user/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
