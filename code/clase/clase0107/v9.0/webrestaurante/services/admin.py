from django.contrib import admin
from services.models import Service, Order


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', )
    ordering = ('title', )
    search_fields = ('title', 'content', )
    list_display = ('title', 'created', )


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )
    ordering = ('name', )
    search_fields = ('name', 'email', )
    list_display = ('name', 'total', 'date', )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
