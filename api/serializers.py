from search.models import Plant
from rest_framework import serializers

# class PlantSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model =Plant
#         fields = ["barcode", "taxon", "country", "collector", "year", "scan"]

class PlantSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'barcode': instance.barcode,
            'title': instance.taxon,
            'country' : instance.country,
            'year' : instance.year,
            'test' : 'testik',
            'type' : 'flora',

        }