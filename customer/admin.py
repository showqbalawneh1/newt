from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from customer import models


@admin.register(models.Client)
class Client(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']