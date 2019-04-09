from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
         return self.name

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "{}".format(self.username)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    register = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
