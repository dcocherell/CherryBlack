from django.urls import path
from . import views  # Import views from current directory

urlpatterns = [
    path('user_input/', views.user_input),  # Define your custom route
]
