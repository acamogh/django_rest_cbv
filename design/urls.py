from django.conf.urls import url,include
from django.contrib import admin

from design import views

urlpatterns = [
    url(r'home/$', views.home, name='home'),
    url(r'api/$', views.PostListAPIView.as_view()),# post list
    url(r'api/(?P<theme_name>[\w-]+)/$', views.PostDetailAPIView.as_view(), name='detail'), # detail
    url(r'api/(?P<theme_name>[\w-]+)/edit/$', views.PostUpdateAPIView.as_view(), name='update'), # update
    url(r'api/(?P<theme_name>[\w-]+)/delete/$', views.PostDeleteAPIView.as_view(), name='delete'),# delete
    url(r'create/$', views.PostCreateAPIView.as_view()) # create

]