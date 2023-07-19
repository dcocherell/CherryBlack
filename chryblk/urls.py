from django.urls import path
from . import views  # Import views from current directory

urlpatterns = [
    path('', views.user_input, name='user_input'),  # Define your custom route
]
