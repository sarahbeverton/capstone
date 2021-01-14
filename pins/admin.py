from django.contrib import admin

from pins.models import Pin, Comment
# Register your models here.

admin.site.register(Pin)
admin.site.register(Comment)