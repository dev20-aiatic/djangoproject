from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UsersCreationForm, UsersChangeForm

# Register your models here.
from .models import Profile


class AccountAdmin(BaseUserAdmin):
    form = UsersChangeForm
    add_form = UsersCreationForm

    list_display = ('email', 'username', 'first_name', 'last_name', 'id_num',
                    'profile_picture', 'password', 'is_active', 'is_staff', 'is_admin')
    list_filter = ('is_active', 'is_admin', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Ajuste de cuenta', {'fields': ('is_active', 'is_staff', 'is_admin')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'id_num', 'profile_picture')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'username', 'password1', 'password2')}),
        ('Ajuste de cuenta', {'fields': ('is_active', 'is_staff', 'is_admin')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'id_num', 'profile_picture')}),
    )

    search_fields = ('email', 'username', 'id_num')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Profile, AccountAdmin)
admin.site.unregister(Group)
