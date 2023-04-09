from django.urls import path
from .views import dashboard, home, login_request, logout_request, register_request
urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name= "logout"),
    path('register', register_request, name='register'),
]
