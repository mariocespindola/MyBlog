"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from MyBlog.accounts import views as logviews
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("MyBlog.comments.urls", namespace='comments')),

    url(r'^register/', logviews.register_view, name='register'),
    url(r'^login/', logviews.login_view, name='login'),
    url(r'^logout/', logviews.logout_view, name='logout'),
    url(r'^', include("MyBlog.posts.urls", namespace='posts')),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/users/', include("MyBlog.accounts.api.urls", namespace='users-api')),
    url(r'^api/comments/', include("MyBlog.comments.api.urls", namespace='comments-api')),
    url(r'^api/posts/', include("MyBlog.posts.api.urls", namespace='posts-api')),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
