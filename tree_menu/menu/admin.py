from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import MenuItem


class MenuItemAdmin(MPTTModelAdmin):
    list_display = ('name', 'url')


admin.site.register(MenuItem, MenuItemAdmin)
