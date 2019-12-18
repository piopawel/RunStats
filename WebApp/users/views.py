from .models import Profile

from django.shortcuts import render
from django.views.generic import ListView


class RunnersListView(ListView):
    model = Profile
    template_name = 'users/runners-list.html'
    context_object_name = 'profiles'
    ordering = ['name']

def profile_view(request, pk):
    context = {'profile': Profile.objects.filter(pk=pk).first()}
    return render(request, 'users/profile.html', context)

