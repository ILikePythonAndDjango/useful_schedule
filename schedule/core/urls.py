from django.urls import path, re_path

from . import views

urlpatterns = (
    path('goals/', views.goals),
    path('goals/<int:pk>/', views.goal, name='goal'),
    path('notes/', views.notes),
    path('notes/<int:pk>/', views.note, name='note'),
    path('things/<int:cost_pk>/', views.cost, name='cost'),
    path('schedules/', views.schedules),
    path('schedules/<int:pk>/', views.schedule, name='schedule'),
)