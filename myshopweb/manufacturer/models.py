from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse
# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/manufacturers')
    status = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.content
    
    def manufacturer_img(self):
        return mark_safe('<img src="{}" width="100" >'.format(self.image.url))
    manufacturer_img.short_description = "Image"
    manufacturer_img.allow_tags = True
    
    def get_absolute_path(self):
        return reverse('product:productlist') + f'?manufacturer_id={self.id}'
    def __str__(self):
        return self.name