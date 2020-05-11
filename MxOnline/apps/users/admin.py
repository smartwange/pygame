from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile

# 将后台管理和表关联起来，就是把models在admin中注册。这样后台即可操作数据



class UserProfileAdmin(admin.ModelAdmin):
    pass

# django自带admin注册方式，使用xadmin时不用书写，自动注册
# UserAdmin django自带用户信息，UserProfileAdmin自定义用户信息
# admin.site.register(UserProfile,UserProfileAdmin)
# admin.site.register(UserProfile,UserAdmin)
# Register your models here.
