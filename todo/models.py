from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=150)
    time = models.TimeField(default=None, null=True)
    completed = models.BooleanField(default=False)
    local = models.CharField(max_length=150, default= None, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
