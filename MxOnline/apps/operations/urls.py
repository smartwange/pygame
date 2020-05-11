from django.conf.urls import url
from apps.operations.views import addFavView


urlpatterns = [
    url(r'^add_fav/$',addFavView.as_view(),name='add_fav')
]
