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
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.views.generic import ListView, RedirectView
from rest_framework import routers
from api import views
from search import models

router = routers.DefaultRouter()
router.register(r"", views.PlantsViewSet)

urlpatterns = [
    path("api/data/<str:barcode>/", views.get_data),
    path("api/list/", views.get_list),
    path("api/src/<str:barcode>/", views.get_src),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(
        "collections",
        ListView.as_view(
            model=models.Plant, paginate_by=12, template_name="collections.html"
        ),
    ),
    re_path("^index", include("index.urls")),
    re_path(r"^search/", include("search.urls")),
    path("admin/", admin.site.urls),
    re_path("^$", include("index.urls")),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True))
]

# if settings.DEBUG:
urlpatterns += [
    url(r"^scans/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, }),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
