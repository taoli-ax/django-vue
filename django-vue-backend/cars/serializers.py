from rest_framework import serializers

from cars.models import CarInfo


class CarInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarInfo
        fields = ['name']
