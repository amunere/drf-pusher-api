from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')

@admin.register(Maillist)
class MaillistAdmin(admin.ModelAdmin):
    list_display = ('text', 'start', 'end', 'phone')

@admin.register(Message)
class MaillistAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'maillist', 'client')
    list_filter = ('status', 'date')
