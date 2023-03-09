from rest_framework.fields import NOT_READ_ONLY_REQUIRED, ReadOnlyField
from main.models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            'category',
            'username',
            'created_at',
            'update_at',
            'type',
            'email',
        ]
        
        read_only_fields = ['created_at', 'update_at', 'id']
