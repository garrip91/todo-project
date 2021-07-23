from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    datecompleted = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время завершения')
    important = models.BooleanField(default=False, verbose_name='Приоритетность')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Список событий"
        verbose_name_plural = "Список событий"
        ordering = ['title']