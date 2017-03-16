from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', "MyBlog.posts.views.post_list"),
    url(r'^create/$', "MyBlog.posts.views.post_create"),
    url(r'^detail/$', "MyBlog.posts.views.post_detail"),
    url(r'^update/$', "MyBlog.posts.views.post_update"),
    url(r'^delete/$', "MyBlog.posts.views.post_delete"),
]
