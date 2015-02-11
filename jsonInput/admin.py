from django.contrib import admin
from models import *

class AccessAdmin(admin.ModelAdmin):
    list_display = ('userId', 'AccessToken')

admin.site.register(payments)
admin.site.register(AccessKeys , AccessAdmin)
