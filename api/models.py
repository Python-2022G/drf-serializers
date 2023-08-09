from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.Case, related_name='tasks')
    

    def __str__(self):
        return f"{self.title} - {self.description[:10]}"