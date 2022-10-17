from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView
from django.views.generic.base import TemplateView
from .filter import ProductFilter
from .models import Category,Product
from manufacturer.models import Manufacturer
from django.db.models import Count
from django.shortcuts import render
# def listing(request):
#     product_list = Product.objects.all()
#     paginator = Paginator(product_list, 25) # Show 25 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'productlist.html', {'page_obj': page_obj})

class ProductList(FilterView):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 20 
    # get_max_amount_products()
    filterset_class = ProductFilter
    context_object_name = 'products'
    template_name = 'productlist.html'
    class Meta:
        ordering = ('id','name')
    def get_queryset(self):
        qs = super().get_queryset()
        if 'category_slug' in self.kwargs:
            qs = qs.filter(category__slug=self.kwargs['category_slug'])
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dscategory'] = Category.objects.all()
        context['dsmanufacturer'] = Manufacturer.objects.all()
        # context['products'] = Product.objects.all()
        return context
class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'productdetails.html'
    context_object_name = 'product'

    def get_queryset(self):
        product = super().get_queryset()
        return product.select_related('category_id').annotate(
            total_purchases=Count('name'))



class CategoriesList(generic.ListView):
    template_name = 'categorylist.html'
    context_object_name = 'categories'
    queryset = Category.objects.all().annotate(num_products=Count('product'))

