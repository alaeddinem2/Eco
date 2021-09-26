from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from student_mnagament_app.models import CustomerUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomerUser,UserModel)
