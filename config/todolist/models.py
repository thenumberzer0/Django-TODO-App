from django.db import models
from django.contrib.auth.models import User


class todo_items(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    time = models.DateField()
    urgency = models.IntegerField()
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        ordering = ['-urgency']

    def __str__(self):
        return self.title
