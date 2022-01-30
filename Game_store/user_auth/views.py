from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


def log_in(request):
    if request.user.is_authenticated:
        return redirect('front_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('front_page')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'home.html', context)


def register(request):
    # if request.user.is_authenticated:
    #     return redirect('front_page')
    # else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account has created for {user}')
                return redirect('front_page')
        context = {'form': form}
        return render(request, 'home.html', context)


def log_out(request):
    logout(request)
    return redirect('front_page')
