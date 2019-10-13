"""lblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_index import views
from django.urls import re_path
from django.views.static import serve
from lblog import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('archive/', views.archive, name= 'archive'),
    path('diary/', views.diary, name= 'diary'),
    path('comments/', views.comments, name= 'comments'),
    path('about/', views.about, name= 'about'),
    path('login/', views.login, name= 'login'),
    path('find/', views.find, name='find'),
    re_path('upload/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT,} ),
    path('upload_img/', views.upload_img, name='upload_img'),
    path('ajax_comment/', views.ajax_comment, name= 'ajax_comment'),
    re_path('diary-article/(?P<did>\d+)', views.diary_article, name='diary_article'),
    re_path('article/(?P<a_id>\d+)', views.article, name= 'article'),
    re_path('tags/(?P<tagid>\d+)', views.tags, name= 'tags'),
]
