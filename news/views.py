from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import News, Comment
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment posted!'
            )

    comment_form = CommentForm()

    return render(request, "news/news_detail.html", {
        "news": news, "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
