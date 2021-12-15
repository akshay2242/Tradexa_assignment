from django.db import models
from django.contrib.auth.models import User as Ur
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    created_place = models.CharField(max_length=50)
    updated_place = models.CharField(max_length=50)
