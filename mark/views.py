from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    print('blog首页')
    return  HttpResponse('<h1>blog首页!</h1>')