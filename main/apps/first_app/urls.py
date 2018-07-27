from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users_api$', views.users_api),
    url(r'^$users_api_json', views.users_api_json),
    url(r'^B$', views.b),   
]      