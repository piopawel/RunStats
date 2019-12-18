from .models import Profile

from django.shortcuts import render
from django.views.generic import ListView


class RunnersListView(ListView):
    model = Profile
    template_name = 'users/runners-list.html'
    context_object_name = 'profiles'
    ordering = ['name']

