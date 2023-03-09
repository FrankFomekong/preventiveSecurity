from rest_framework.fields import NOT_READ_ONLY_REQUIRED, ReadOnlyField
from main.models import Report
from rest_framework import serializers

class ReportSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Report
        fields = [
            'id',
            'crop_type',
            'created_at',
            'update_at',
            'month',
            'plot',
            'operator',
	    'income',
        ]
        read_only_fields = ['created_at', 'update_at', 'id']
