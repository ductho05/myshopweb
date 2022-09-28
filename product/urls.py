from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [
    path('',views.ProductList.as_view(),name = 'productlist'),
    path('categories',views.CategoriesList.as_view(),name ='categorylist'),
    path('details',views.ProductDetails.as_view(),name = 'productdetails'),
]
