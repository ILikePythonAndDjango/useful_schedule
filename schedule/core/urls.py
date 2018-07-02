from django.urls import path, re_path

from . import views

urlpatterns = (
    path('goals/', views.goals, name='goals'),
    path('goals/<int:pk>/', views.goal, name='goal')
)