from django.urls import path
from . import views
from .views import FeedBackViews

app_name = 'feedback'
urlpatterns = [
    path('',FeedBackViews.as_view(),name = 'feedback_form')
]