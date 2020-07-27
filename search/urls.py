from django.urls import path, re_path
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    re_path(r"search_result", views.search.as_view(), name="search_result"),
    # url(r'services/(?P<plant_id>\D+)', views.services),
    path(r"services/<str:barcode>", views.services),
    re_path(r"^$", views.home.as_view()),
]
if settings.DEBUG:
    urlpatterns += [
        url(r"^scans/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, }),
    ]
