from django.urls import path
from . import views

urlpatterns = [
    path('', views.userInitialezed, name='userInitialized'),
    path('hello/', views.hello, name='hello'),
]