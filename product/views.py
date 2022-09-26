from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView
from .filter import ProductFilter
from .models import Category,Product
from django.db.models import Count
from django.core.paginator import Paginator
from django.shortcuts import render
def produclist(request):
    content = {}
    categorys = Category.objects.all()
    content['categorys'] = categorys
    return render(request,'product/productlist.html',content)


class ProductList(FilterView):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 20 
    # get_max_amount_products()
    filterset_class = ProductFilter
    context_object_name = 'products'
    template_name = 'productlist.html'

class CategoriesList(generic.ListView):
    template_name = 'categorylist.html'
    context_object_name = 'categories'
    queryset = Category.objects.all().annotate(num_products=Count('product'))
