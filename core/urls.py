from django.urls import path
from .views import dashboard, home, login, signup
urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
