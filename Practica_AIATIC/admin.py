from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

from .models import User
from .forms import UsersCreationForm, UsersChangeForm


class AccountAdmin(BaseUserAdmin):
    form = UsersChangeForm
    add_form = UsersCreationForm

    list_display = ('email', 'username', 'first_name', 'last_name', 'id_num',
                    'profile_picture', 'password', 'is_active', 'is_staff', 'is_admin')
    list_filter = ('is_active', 'is_admin', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'is_active', 'is_staff', 'is_admin', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'id_num', 'profile_picture')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'username', 'is_active', 'is_staff', 'is_admin', 'password1', 'password2')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'id_num', 'profile_picture')}),
    )

    search_fields = ('email', 'username', 'id_num')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, AccountAdmin)
