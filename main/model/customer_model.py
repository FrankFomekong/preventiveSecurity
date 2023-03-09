from django.db import models
from .basic_model import BasicClass


class Customer(BasicClass):
   TYPE = (('admin','admin'),
	('operator','operator')
   )
   
   username = models.TextField(null=False)
   email = models.TextField(null=False,unique=True)
   type = models.CharField(max_length=20,choices=TYPE,default='admin')
   category = models.TextField(null=True)
   
