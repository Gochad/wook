from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import NewUserForm, UpdateUserForm, UpdateProfileForm


def dashboard(request):
    return render(request, 'dashboard.html', {})

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html', {})

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('dashboard')
        messages.error(request, 'Unsuccessful registration. Invalid information')

    form = NewUserForm()
    return render(request, 'register.html', {'register_form': form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})

def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(request.user)
        profile_form = UpdateProfileForm(request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
