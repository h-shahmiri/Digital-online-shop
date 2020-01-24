from django.contrib import admin
from .models import *

# Register your models here.

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('state_choice','city_choice','address', 'post_code','id')

    list_filter  = ['city_choice' , 'post_code']
admin.site.register(UserAddress , UserAddressAdmin)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','national_code','address', 'phone_numb', 'email', 'score','id')

    list_filter  = ['national_code' , 'score']
admin.site.register(Profile ,ProfileAdmin)

