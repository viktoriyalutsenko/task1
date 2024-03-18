from django.urls import path
from .views import task_list, create_task, edit_task, register, user_login, logout_view

urlpatterns = [
    path('', task_list, name='login'),
    path('create/', create_task, name='create_task'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('register/', register, name='register'),  # URL-адрес для регистрации
    path('login/', user_login, name='login'),  # URL-адрес для входа
    path('logout/', logout_view, name='logout'),
    path('task-list/', task_list, name='task_list'),
]
