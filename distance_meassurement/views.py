from django.shortcuts import render
from search.models import Plant
from django.db.models import Q

# Create your views here.
def meassurement(request, barcode):

    plant = Plant.objects.get(barcode=barcode)

    return render(request, 'meassurement.html', {'plant': plant})

