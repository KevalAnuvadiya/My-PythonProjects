from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    taskID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    nm = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    em1 = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.nm + '-' + self.em1
    
    