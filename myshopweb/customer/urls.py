import imp
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
app_name = 'customer'

urlpatterns = [
    path("register/",views.Register,name="register"),
    path('login/', LoginView.as_view(template_name = 'login.html'),name="login"),
    path('logout/', LogoutView.as_view(next_page = '/'),name="logout")
]