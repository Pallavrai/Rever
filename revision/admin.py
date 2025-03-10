from django.contrib import admin
from .models import UserProfile, Problem

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Problem)