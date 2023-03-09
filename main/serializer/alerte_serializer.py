from rest_framework.fields import NOT_READ_ONLY_REQUIRED, ReadOnlyField
from main.models import Alerte
from rest_framework import serializers

class AlerteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Alerte
        fields = [
            'id',
            'message',
            'created_at',
            'update_at',
            'photo',
            'id_detection'
        ]
        
        read_only_fields = ['created_at', 'update_at', 'id']
