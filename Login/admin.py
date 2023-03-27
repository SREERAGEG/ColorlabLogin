from django.contrib import admin
from . models import UserData
# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    list_display=('email','passwd')
admin.site.register(UserData,UserDataAdmin)