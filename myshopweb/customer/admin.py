from django.contrib import admin
from product.models import Category
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['id']
    search_fields = ('name',)
admin.site.register(Category, SettingAdmin)