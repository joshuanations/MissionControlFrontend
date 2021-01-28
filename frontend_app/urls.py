from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='frontend_app-home'),
    path('about/', views.about, name='frontend_app-about'),
]