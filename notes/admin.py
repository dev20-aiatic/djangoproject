from django.contrib import admin

# Register your models here.
from notes.models import Board, Ideas

admin.site.register(Board)
admin.site.register(Ideas)
