from django.urls import path,reverse_lazy,include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import ProfileView,PasswordChangeView,MyLoginView
from . import views
app_name = 'customer'

urlpatterns = [
    path("register/",views.Register,name="register"),
    path('', include('social_django.urls', namespace='social')),
    path('login/', MyLoginView.as_view(template_name = 'login.html'),name="login"),
    path('logout/', LogoutView.as_view(next_page = '/',),name="logout"),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('password-change/', PasswordChangeView.as_view(),name='password-change'),
    
    # path('profile', views.profile, name='profile')
]