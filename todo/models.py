from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    time = models.TimeField(default=None, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
