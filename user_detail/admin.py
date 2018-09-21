from django.contrib import admin
from .models import UserProfile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    list_display = ['Name', 'Email','Mobile','Address','Gender','Bloodgroup','Dob']
    search_fields = ['Name', 'Email']


admin.site.register(UserProfile, ProfileAdmin)
