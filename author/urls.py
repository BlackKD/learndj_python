from django.conf.urls import url, include
from author import views

urlpatterns = [
    url(r'^$', views.home_page, name="home"),
    url(r'^([a-zA-Z_]+)/', views.user_page, name="author"),
    url(r'^search$', views.search, name="search"),
    url(r'^check',views.checkchapter,name ="checkchapter"),
]
