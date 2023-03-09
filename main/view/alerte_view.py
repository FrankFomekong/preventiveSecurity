import main
from main.serializer.alerte_serializer import AlerteSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes

from ..exceptions import *
from main.serializers import *
from main.models import *

class AlerteViewSet(viewsets.ModelViewSet):
    queryset = Alerte.objects.all()
    serializer_class = AlerteSerializer
    filter_backends = [SearchFilter, OrderingFilter]
