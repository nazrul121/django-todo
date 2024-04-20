from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsDone/<int:pk>/', views.markAsDone, name='mark-as-done'),
    path('edit-task/<int:pk>/', views.editTask, name='edit-task'),
    path('update-task/<int:pk>/', views.updateTask, name='update-task'),
    path('delete-task/<int:pk>/', views.deleteTask, name='delete-task'),
    
]
