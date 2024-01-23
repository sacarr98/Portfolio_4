from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def the_news(request):
    return HttpResponse("Hello, World!")
