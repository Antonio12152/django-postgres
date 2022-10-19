from .models import Post, Text
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, Http404


# Create your views here.


def post_lists(request):
    posts = Post.objects.all()
    # user_name = ''
    # if request.GET:
    #     user_name = request.GET['name']
    return render(request, 'blog/index.html', context={'posts': posts})


# def text_lists(request):
#     texts = Text.objects.all()
#     return render(request, 'blog/index.html', context={'texts': texts})


def pageNotFound(request, exemption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def checkName(request):
    raise Http404
