from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Plant
from django.db.models import Q

class search(ListView):
    model = Plant
    template_name ='search_result.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Plant.objects.filter(
            Q(name__icontains= query) | Q(id_of_plant__icontains = query)
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
def services(request, plant_id):
    print('sdsd:',plant_id)
    #plant_id='mini'
    plant = Plant.objects.get(Q(id_of_plant__icontains=plant_id))

    return render(request, 'services.html',{'plant':plant})

