from django.urls import path, include
from . import views
from .views import health_check, metrics

app_name = 'chryblk'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('input_financial_data/', views.input_financial_data, name='input_financial_data'),
    path('report/', views.report, name='report'),
    path('logout/', views.logout_view, name='logout'),
    path('health_check/', health_check, name='health_check'),
    path('metrics/', metrics, name='metrics'),
]
