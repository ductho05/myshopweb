from django.db import models
from django.urls import reverse
from customer.models import Category
from django.utils.html import mark_safe
from manufacturer.models import Manufacturer
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.content
    def __str__(self):
        return self.name
    def get_absolute_path(self):
        return reverse('product:productlist') + f'?category_id={self.id}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 

   
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to = "myshopweb/images/products")
    size = models.CharField(max_length=6, default='')
    material = models.CharField(max_length=20,default='')
    sleeve_length = models.CharField(max_length=20, default='')
    season = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=1000)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Manufacturer")
    status = models.IntegerField(default=0, blank= True )
    def __unicode__(self):
        return self.content
    
    def product_img(self):
        return mark_safe('<img src="{}" width="100" >'.format(self.image.url))
    product_img.short_description = "Image"
    product_img.allow_tags = True
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product:productdetails', kwargs={'pk': self.id})
