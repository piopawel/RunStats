from django.urls import path
from . import views

urlpatterns = [
    path('', views.RunnersListView.as_view(), name='runners-list'),
    path('<int:pk>/', views.profile_view, name='runner-profile'),
]