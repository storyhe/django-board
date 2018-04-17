from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.board_post, name='board_list'),
    path('<str:board_name>/', views.board_posts, name="board_posts"),
    path('<str:board_name>/write', views.board_write, name='board_write')
]