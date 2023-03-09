from rest_framework.fields import NOT_READ_ONLY_REQUIRED, ReadOnlyField
from main.models import Plot
from rest_framework import serializers

class PlotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Plot
        fields = [
            'id',
            'name',
            'created_at',
            'update_at',
            'location',
            'area',
            'photo',
            'owner',
        ]
        read_only_fields = ['created_at', 'update_at', 'id']
