from django.contrib import admin
from feedback.models import Feedback
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'subject_name', 'contents', 'status')
    list_display_links = ('id', 'name', 'email', 'phone', 'subject_name', 'contents', 'status')
    list_filter = ('status',)
    list_per_page = 5
    ordering = ['id']
    search_fields =  ('name',)

admin.site.register(Feedback, SettingAdmin)