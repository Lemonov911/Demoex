from django.contrib import admin
from accounts.models import Role
from .models import Supplies, Application, Item


@admin.register(Supplies)
class SuppliesAdmin(admin.ModelAdmin):
    pass


class ItemsInline(admin.TabularInline):
    model = Item
    extra = 1
    readonly_fields = (
        'application',
    )
    fields = (
        'item',
        'number',
    )

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    inlines = [ItemsInline]
    list_display = (
        "__str__",
        "client",
        "manager",
    )
    list_filter = (
        "manager",
    )