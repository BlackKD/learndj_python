from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^signin$', views.signin_view, name='signin'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
]