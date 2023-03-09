import main
from main.serializer.report_serializer import ReportSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes

from ..exceptions import *
from main.serializers import *
from main.models import *

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['croptype', 'month', 'plot','operator', 'id','income']
