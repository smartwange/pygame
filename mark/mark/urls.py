"""mark URL Configuration

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
"""为mark定义URL模式"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

# 导入视图
# import views

app_name = 'mark'

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置路由信息，当用户访问index路径时，则表示有views.index函数类处理
    # url(r'^index/',views.index,name='index')
    url(r'^blog/', include('blog.urls')),
]
