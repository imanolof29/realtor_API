from django.contrib import admin
from users.models import RequestLog

# Register your models here.


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'url', 'remote_address', 'method', 'date']

admin.site.register(RequestLog, RequestLogAdmin)
