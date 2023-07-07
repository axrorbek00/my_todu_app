from django.db import models
from users.models import UsersModel
from ckeditor.fields import RichTextField


class CategoriyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ToduModel(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.RESTRICT)
    task_name = models.CharField(max_length=225)
    description = RichTextField()
    task_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['-created_at']
