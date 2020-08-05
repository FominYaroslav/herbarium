from django.shortcuts import render
from search.models import Plant
from .serializers import PlantSerializer
from rest_framework import viewsets
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser
from django.http import HttpResponseRedirect, HttpResponse
from dicttoxml import dicttoxml
from lxml.etree import Element, SubElement, QName, tostring
import json

class XMLNamespaces:
    dc = "http://purl.org/dc/elements/1.1/"
    edm = "http://www.europeana.eu/schemas/edm/"
    rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    wgs84_pos = "http://www.w3.org/2003/01/geo/wgs84_pos#"
    foaf = "http://xmlns.com/foaf/0.1/"
    rdaGr2 = "http://rdvocab.info/ElementsGr2/"
    oai = "http://www.openarchives.org/OAI/2.0/"
    owl = "http://www.w3.org/2002/07/owl#"
    ore = "http://www.openarchives.org/ore/terms/"
    skos = "http://www.w3.org/2004/02/skos/core#"
    dcterms = "http://purl.org/dc/terms/"


class PlantsViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)


def get_list(request):
    response = {
        "barcodes": []
    }

    for plant in Plant.objects.all():
        response["barcodes"].append(plant.barcode)
    return HttpResponse(json.dumps(response), content_type="application/json")


def get_src(request, barcode):
    plant = Plant.objects.get(barcode=barcode)
    data = plant.scan.read()
    return HttpResponse(data, content_type="image/jpeg")


def get_data(request, barcode):
    plant = Plant.objects.get(barcode=barcode)

    identifier = "#UEDIN:" + barcode

    root = Element(QName(XMLNamespaces.rdf, 'RDF'), nsmap
    ={
        'edm': XMLNamespaces.edm,
        'rdf': XMLNamespaces.rdf,
        'dc': XMLNamespaces.dc,
        'wgs84_pos': XMLNamespaces.wgs84_pos,
        'foaf': XMLNamespaces.foaf,
        'rdaGr2': XMLNamespaces.rdaGr2,
        'oai': XMLNamespaces.oai,
        'owl': XMLNamespaces.owl,
        'ore': XMLNamespaces.ore,
        'skos': XMLNamespaces.skos,
        'dcterms': XMLNamespaces.dcterms
    })

    cho = SubElement(root, QName(XMLNamespaces.edm, 'ProvidedCHO'))
    cho.attrib[QName(XMLNamespaces.rdf, 'about')] = identifier

    dcDate = SubElement(cho, QName(XMLNamespaces.dc, 'date'))
    dcDate.text = str(plant.year)

    dcTitle = SubElement(cho, QName(XMLNamespaces.dc, 'title'))
    dcTitle.text = plant.taxon

    dcIdentifier = SubElement(cho, QName(XMLNamespaces.dc, 'identifier'))
    dcIdentifier.text = identifier

    dctermsSpatial = SubElement(cho, QName(XMLNamespaces.dcterms, 'spatial'))
    dctermsSpatial.text = plant.country

    dcCoverage = SubElement(cho, QName(XMLNamespaces.dc, 'coverage'))
    dcCoverage.text = plant.locality

    dcContributor = SubElement(cho, QName(XMLNamespaces.dc, 'contributor'))
    dcContributor.text = plant.collector

    dcCreator = SubElement(cho, QName(XMLNamespaces.dc, 'creator'))
    dcCreator.text = plant.legend_author

    dcPublisher = SubElement(cho, QName(XMLNamespaces.dc, 'publisher'))
    dcPublisher.text = 'Comenius University'

    dcType = SubElement(cho, QName(XMLNamespaces.dc, 'type'))
    dcType.text = 'Plant'

    edmType = SubElement(cho, QName(XMLNamespaces.edm, 'type'))
    edmType.text = 'IMAGE'

    edmWebResource = SubElement(root, QName(XMLNamespaces.edm, 'WebResource'))
    edmWebResource.attrib[QName(XMLNamespaces.rdf, 'about')] = "/api/src/" + barcode + "/"

    edmRights = SubElement(edmWebResource, QName(XMLNamespaces.edm, 'rights'))
    edmRights.attrib[QName(XMLNamespaces.rdf, 'resource')] = "https://creativecommons.org/licenses/by-nc-sa/4.0/"

    oreAggregation = SubElement(root, QName(XMLNamespaces.ore, 'Aggregation'))
    oreAggregation.attrib[QName(XMLNamespaces.rdf, 'about')] = "/search/services/" + barcode + "/"

    edmCHO = SubElement(oreAggregation, QName(XMLNamespaces.edm, 'aggregatedCHO'))
    edmCHO.attrib[QName(XMLNamespaces.rdf, 'resource')] = identifier

    edmDataProvider = SubElement(oreAggregation, QName(XMLNamespaces.edm, 'dataProvider'))
    edmDataProvider.text = "Comenius University"

    edmIsShownBy = SubElement(oreAggregation, QName(XMLNamespaces.edm, 'isShownBy'))
    edmIsShownBy.attrib[QName(XMLNamespaces.rdf, 'resource')] = "/api/src/" + barcode + "/"

    edmProvider = SubElement(oreAggregation, QName(XMLNamespaces.edm, 'provider'))
    edmProvider.text = "Comenius University"

    edmRights_2 = SubElement(oreAggregation, QName(XMLNamespaces.edm, 'rights'))
    edmRights_2.attrib[QName(XMLNamespaces.rdf, 'resource')] = "https://creativecommons.org/licenses/by-nc-sa/4.0/"

    return HttpResponse(tostring(root), content_type='text/xml')