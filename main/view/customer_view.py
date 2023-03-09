import main
from main.serializer.customer_serializer import CustomerSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes

from ..exceptions import *
from main.serializers import *
from main.models import *

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email', 'type', 'id']
    filter_fields = ['username', 'email', 'type', 'id']


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    """
        allow user here land owner or operator to login
    """
    if (("email" not in request.data) or ("password" not in request.data)):
        
        result = {
            "status": False,
            "message": "Please provide fileds email and password for corret login",
            "data":{}
        }
        return Response(result, status=status.HTTP_200_OK)
    
    #try:
    customer = Customer.objects.filter(email=request.data["email"]).filter(password=request.data["password"])
    custumer=CustomerSerializer(customer[0])
    #print(custumer.data)
    #print(custumer)
    out=custumer.data
    del out["password"]
    result = {
            "status": True,
            "message": "acount type information are in data",
            "data":out 
    }
    return Response(result, status=status.HTTP_200_OK)
    #except:
     #   result = {
      #      "status": False,
       #     "message": "Une erreur est survenu.",
        #    "data": {}
        #}
        #return Response(result, status=status.HTTP_500)

