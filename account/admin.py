from django.contrib import admin
from .models import Department, Profile, User

# Register your models here.
admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(User)
