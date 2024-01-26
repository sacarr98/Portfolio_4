from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import News

# Create your views here.


class NewsList(generic.ListView):
    queryset = News.objects.all()
    template_name = "news/index.html"
    pagniate_by = 6


def news_detail(request, slug):
    """
    Display an individual :model:`news.News`.

    **Context**

    ``news``
        An instance of :model:`news.News`.

    **Template:**

    :template:`news/news_detail.html`
    """
    queryset = News.objects.filter(status=1)
    news = get_object_or_404(queryset, slug=slug)
    return render(request, "news/news_detail.html", {"news": news},)
