from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
def dashboard(request):
    return render(request, 'dashboard.html', {})