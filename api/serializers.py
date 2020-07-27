from rest_framework import serializers


class PlantSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'barcode': instance.barcode,
            'title': instance.taxon,
            'country': instance.get_country_display(),
            'year': instance.year,
            'test': 'testik',
            'type': 'flora',

        }