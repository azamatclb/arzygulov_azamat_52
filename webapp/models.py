from django.db import models


# Create your models here.

class ToDoList(models.Model):
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=150, null=False, blank=False, default='new', verbose_name='Статус')
    deadline = models.DateField(verbose_name='Дедлайн')

    def __str__(self):
        return f"{self.id}. {self.description} {self.status} {self.deadline}"
        pass

    class Meta:
        db_table = "todo list"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
