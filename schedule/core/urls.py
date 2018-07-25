from django.urls import path, re_path

from . import views

urlpatterns = (
    path('goals/', views.goals),
    path('goals/<int:pk>/', views.goal, name='goal'),
    path('notes/', views.notes),
    path('notes/<int:pk>/', views.note, name='note'),
    path('things/<int:pk>/', views.cost, name='cost'),
    path('schedules/', views.schedules),
    path('schedules/<int:pk>/', views.schedule, name='schedule'),
    path('login/', views.log_in),
    path('logout/', views.log_out),
    path('signup/', views.sign_up)
)