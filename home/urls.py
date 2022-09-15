from turtle import home
from django.urls import path
from.views import home, create_todo, read_todo, update_todo, delete_todo

urlpatterns = [
  path('', home, name='home'),
  path('create/', create_todo, name='todo_create'),
  path('read/<int:pk>/', read_todo, name='todo_read'),
  path('update/<int:pk>/', update_todo, name='todo_update'),
  path('delete/<int:pk>/', delete_todo, name='todo_delete'),
]