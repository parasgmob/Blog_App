from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # importing django default user model

# Create your models here.
class user(models.Model):
    pass

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) #auto_now_add=True
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #dunder method or magic method
        return self.title

#See SQL code for migrations "python manage.py sqlmigrate app_name file_name(0001)" 
# Rull shell using "python manage.py shell"
# user.post_set