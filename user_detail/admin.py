from django.contrib import admin
from .models import UserProfile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    list_display = ['name', 'email','mobile','address','gender','blood_group','dob']
    search_fields = ['name', 'email']


admin.site.register(UserProfile, ProfileAdmin)
