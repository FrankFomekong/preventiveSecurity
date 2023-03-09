from rest_framework.fields import NOT_READ_ONLY_REQUIRED, ReadOnlyField
from main.models import Detection
from rest_framework import serializers

class DetectionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Detection
        fields = [
            'id',
            'idPersonne',
            'created_at',
            'update_at',
            'status'
        ]
        
        read_only_fields = ['created_at', 'update_at', 'id']
