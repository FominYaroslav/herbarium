from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Plant
from django.db.models import Q

class search(ListView):
    model = Plant
    template_name ='search_result.html'
    def get_queryset(self):
        taxon_get = self.request.GET.get('taxon')
        country_get = self.request.GET.get('country')
        barcode_get = self.request.GET.get('barcode')


        return Plant.objects.filter(
            Q(country__icontains = country_get) & Q(taxon__icontains= taxon_get) & Q(barcode__icontains = barcode_get)

        )
# Create your views here.

class home(TemplateView):

    model = Plant
    template_name = "search.html"

# class services(TemplateView):
#     model = Plant
#     template_name = 'services.html'
#     def get(self, request):
#         print(request.data)
#         plant_id='mini'
#         plant= Plant.objects.get(Q(id_of_plant__icontains = plant_id))
#         return render(request, self.template_name, {'plant':plant})
def services(request, barcode):
    print('sdsd:',barcode)
    #     plant = list(Plant.objects.get(Q(id_of_plant__icontains=plant_id)))

    plant = Plant.objects.get(barcode=barcode)

    return render(request, 'services.html',{'plant':plant})

class collections(ListView):
    model = Plant
    template_name = 'collections.html'





