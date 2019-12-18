from django.urls import path
from . import views

urlpatterns = [
    path('', views.runners_list, name='runners-list'),
]