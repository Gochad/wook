from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.generic import UpdateView


def dashboard(request):
    return render(request, 'dashboard.html', {})

def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'home.html', {})
def signup(request):
    return render(request, 'home.html', {})

class UserUpdateView(UpdateView):
    pass