from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    return render(request, 'index.html')

def articles(request):
    arts=models.Article.objects.all()
    return render(request,'article.html',{'arts':arts})

def articleDetail(request,art_id):
    art=models.Article.objects.get(pk=art_id)
    return render(request, 'articleDetail.html', {'art': art})

def editArt(request,art_id):
    art = models.Article.objects.get(pk=art_id)
    return render(request, 'articleModfy.html', {'art': art})