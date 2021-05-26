from django.contrib import admin

# Register your models here.
from .models import MyUser, Profile

admin.site.register(MyUser)
admin.site.register(Profile)
