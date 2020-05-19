from django.shortcuts import render
from search.models import Plant

# Create your views here.
def picker(request, barcode):
    plant = Plant.objects.get( barcode = barcode)
    return render(request, 'color picker.html', {'plant':plant})
