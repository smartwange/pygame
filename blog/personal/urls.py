from django.urls import path
from . import views
app_name='personal'
urlpatterns = [
    path('index', views.index),
    path('article', views.articles),
    path('articleDetail/<art_id>', views.articleDetail,name='article_detail'),
    path('articleModfy/<art_id>', views.editArt,name='article_edit'),
]
