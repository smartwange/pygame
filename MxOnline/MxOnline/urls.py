"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
import xadmin
# 引入静态文件处理方法 serve
from django.views.static import serve

# 使用django默认方法，导向视图文件
# 简写方式 path('login/', TemplateView.as_view(template_name='login.html'),name='login'),
from django.views.generic import TemplateView

from apps.users.views import LoginView,LogoutView
# from apps.organizations.views import orgList
from MxOnline.settings import MEDIA_ROOT

#  cbv(class base view)：类中  fbv(function base view)：留言板
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('register/', TemplateView.as_view(template_name='register.html'),name='register'),
    url(r'^captcha/', include('captcha.urls')),
    # 机构相关页面
    url('^org/',include(('apps.organizations.urls','organizations'),namespace='org')),
    #媒体文件访问路径 path就是文件存储路径
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
#     个人操作
    url('^op/',include(('apps.operations.urls','operations'),namespace='op')),
]
