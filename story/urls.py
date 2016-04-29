from django.conf.urls import url, include
from story import views

urlpatterns = [
    url(r'^new_story$', views.new_story, name='newstory'),
    url(r'^view_story/(\d+)$', views.view_story, name='viewstory'),
    url(r'^new_chapter/(\d+)$', views.new_chapter, name='newchapter'),
    url(r'^change_chapter/(\d+)/(\d+)$', views.change_chapter, name='changechapter'),
]
