from django.shortcuts import render
from search.models import Plant
from .serializers import PlantSerializer
from rest_framework import viewsets
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser


class PlantsViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)




# Create your views here.
