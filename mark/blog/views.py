from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def read(request):
    return HttpResponse('<h2>66666666</h2>')


def greet(request):
    params = {'names': '张三'}
    return render(request, 'blog/index.html', params)

