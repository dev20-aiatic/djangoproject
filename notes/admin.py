from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from notes.models import Board, Ideas


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'status', 'created_at', 'updated_at')

    list_filter = 'status'

    fieldsets = (
        (None, {'fields': ('name', 'user', 'status', 'created_at', 'updated_at')}),
    )

    search_fields = ('name', 'user', 'status')
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(Board)
admin.site.register(Ideas)