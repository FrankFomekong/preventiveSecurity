import main
from main.serializer.plot_serializer import PlotSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes

from ..exceptions import *
from main.serializers import *
from main.models import *

class PlotViewSet(viewsets.ModelViewSet):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'location', 'area', 'owner']
