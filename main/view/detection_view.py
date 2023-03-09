import main
from main.serializer.detection_serializer import DetectionSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes

from ..exceptions import *
from main.serializers import *
from main.models import *

class DetectionViewSet(viewsets.ModelViewSet):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    
