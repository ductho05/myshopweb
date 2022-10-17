from django.contrib import admin
from product.models import Product
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'product_img', 'status')
    list_display_links = ('id', 'name', 'price', 'product_img', 'status')
    list_filter = ('category_id','manufacturer_id',)
    list_per_page = 5
    sortable_by = ['id']
    search_fields = ('name',)

admin.site.register(Product, SettingAdmin)