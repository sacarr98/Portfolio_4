from django.shortcuts import render
from django.views import generic
from .models import News

# Create your views here.


class NewsStories(generic.ListView):
    queryset = News.objects.filter(status=1)
    template_name = "news_stories.html"
