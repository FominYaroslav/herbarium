from django.urls import path
from . import views


urlpatterns = [

    path(r'<str:barcode>',views.picker),

]