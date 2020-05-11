from django.urls import path
import views
from blog import views as bviews

app_name = 'blog'
urlpatterns = [
    path('index/',views.index,name='blog首页'),
    path('read/',bviews.read,name='blog详情页'),
    path('greet/',bviews.greet,name='问候页'),
]