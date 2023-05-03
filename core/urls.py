from django.urls import path
from .views import dashboard, home, profile
urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
]

