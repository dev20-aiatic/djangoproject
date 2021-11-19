from urllib import request

from django.contrib import admin

# Register your models here.
from notes.models import Board, Ideas


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('user', 'status')
    list_per_page = 8

    fieldsets = (
        (None, {'fields': ('name', 'user', 'status')}),
    )

    search_fields = ('name', 'status')
    ordering = ('id',)
    filter_horizontal = ()


class IdeasAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'board', 'created_at', 'updated_at')
    list_filter = ('user', 'board')
    list_per_page = 8

    fieldsets = (
        (None, {'fields': ('title', 'content', 'user', 'board')}),
    )

    search_fields = ('title', 'content')
    ordering = ('id',)
    filter_horizontal = ()


# Registramos la clase del admin con los modelos asociados
admin.site.register(Board, BoardAdmin)
admin.site.register(Ideas, IdeasAdmin)
