from django.urls import path, include
from . import views

app_name = 'chryblk'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('input_financial_data/', views.input_financial_data, name='input_financial_data'),
    path('report/', views.report, name='report'),
    path('logout/', views.logout_view, name='logout'),
]
