from django.contrib import admin

# Register your models here.
from website.models import Contact, Feedback

admin.site.register(Contact)
admin.site.register(Feedback)