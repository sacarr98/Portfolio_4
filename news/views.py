from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import News
from .forms import CommentForm

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
    comments = news.comments.all().order_by("-created_on")
    comment_count = news.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.news = news
            comment.save()

    comment_form = CommentForm()

    return render(request, "news/news_detail.html", {
        "news": news, "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
    )
