from django.shortcuts import render
from django.views import generic
from .models import News

# Create your views here.


class NewsList(generic.ListView):
    queryset = News.objects.all()
    template_name = "news/index.html"
    pagniate_by = 6
