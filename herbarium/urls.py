"""herbarium URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import  settings
from django.views.static import serve
from django.views.generic import TemplateView

from search import views

urlpatterns = [

    # re_path('^index', TemplateView.as_view(template_name= 'index.html')),
    re_path('^index', include('index.urls')),
    re_path('^color_picker/', include('color_picker.urls')) ,
    re_path(r'^search/', include('search.urls')),
    re_path(r'^meassurement/', include('distance_meassurement.urls')),

    # url(r'^search_result', views.search.as_view(), name='search_result'),
    # url(r'^search', views.home.as_view()),

    path('admin/', admin.site.urls),
    re_path('^$',include('index.urls'))
]

if settings.DEBUG:
    urlpatterns+=[url(r'^scans/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    }),]
# оця фігня треба для роботи зображення