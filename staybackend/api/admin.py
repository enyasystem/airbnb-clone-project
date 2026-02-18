from django.contrib import admin

from staybackend.api.models import HealthCheck


@admin.register(HealthCheck)
class HealthCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
