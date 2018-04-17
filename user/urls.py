from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login$', views.login, name='login'),
    url(r'^join$', views.join, name='join'),
    url(r'^logout', views.logout, name='logout')
]