from django.urls import path
from .views import dashboard, home, login_request, register_request
urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
]
