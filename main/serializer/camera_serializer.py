from rest_framework.fields import NOT_READ_ONLY_REQUIRED, ReadOnlyField
from main.models import Camera
from rest_framework import serializers

class CameraSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Camera
        fields = [
            'id',
            'description',
            'created_at',
            'update_at',
            'position',
            'etat'
        ]
        
        read_only_fields = ['created_at', 'update_at', 'id']
