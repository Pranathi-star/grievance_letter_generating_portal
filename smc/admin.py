from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Letter)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = SmcRegisterForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional details',
            {
                'fields':(
                    'name', 
                    'phone_number',
                    'state',
                    'city',
                    'school'
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)