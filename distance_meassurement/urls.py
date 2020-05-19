from django.conf.urls import url, include
from django.urls import path, re_path
from . import views


urlpatterns = [
    path(r'<str:barcode>', views.meassurement),

]