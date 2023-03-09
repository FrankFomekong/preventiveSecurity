from rest_framework.fields import NOT_READ_ONLY_REQUIRED, ReadOnlyField
from main.models import Category
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created_at',
            'update_at',
            'description'
        ]
        
        read_only_fields = ['created_at', 'update_at', 'id']
