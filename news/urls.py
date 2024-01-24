from . import views
from django.urls import path

urlpatterns = [
    path('', views.NewsStories.as_view(), name='home'),
]
