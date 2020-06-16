from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Plant
from django.db.models import Q

class search(ListView):
    model = Plant
    template_name ='search_result.html'
    paginate_by = 12

    def get_queryset(self):

        taxon_get = self.request.GET.get('taxon')
        country_get = self.request.GET.get('country')
        barcode_get = self.request.GET.get('barcode')
        collector_get = self.request.GET.get('collector')
        locality_get =self.request.GET.get('locality')
        year_get = self.request.GET.get('year')

        return Plant.objects.filter(
            Q(country__icontains = country_get) & Q(taxon__icontains= taxon_get) & Q(barcode__icontains = barcode_get)
            &(Q(collector__icontains=collector_get)|Q(legend_author = collector_get)) & Q(locality__icontains = locality_get) & Q(year__icontains = year_get)

        )
# Create your views here.

class home(TemplateView):

    model = Plant
    template_name = "search.html"


def services(request, barcode):
    print('sdsd:',barcode)
    plant = Plant.objects.get(barcode=barcode)
    return render(request, 'services.html',{'plant':plant})








