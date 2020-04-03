from django.shortcuts import render
from search.models import Plant
from django.db.models import Q

# Create your views here.
def meassurement(request, plant_id):
    plant = Plant.objects.get(Q(id_of_plant__icontains=plant_id))

    return render(request, 'meassurement.html', {'plant': plant})

