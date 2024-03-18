from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте дополнительные поля профиля пользователя, если необходимо

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)  # Поле для срока выполнения
    completed = models.BooleanField(default=False)  # Поле для отметки о выполнении
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='LOW')  # Поле для приоритета
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
