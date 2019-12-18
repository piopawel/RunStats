from django.shortcuts import render

def runners_list(request):
    return render(request, 'users/runners-list.html')
