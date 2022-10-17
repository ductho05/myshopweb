from django.contrib import admin
from manufacturer.models import Manufacturer
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'phone', 'manufacturer_img','status')
    list_display_links = ('id', 'name', 'phone', 'address', 'manufacturer_img', 'status')
    list_filter = ('name',)
    list_per_page = 5
    ordering = ['id']
    search_fields = ('name',)

admin.site.register(Manufacturer, SettingAdmin)