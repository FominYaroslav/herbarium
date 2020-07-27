from django.shortcuts import render
from search.models import Plant


def home(request):
    plants = Plant.objects.all()
    context = {"plants": [plant for plant in plants[:10]]}
    return render(request, 'index.html', context)
