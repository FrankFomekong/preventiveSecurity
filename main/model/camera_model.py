from django.db import models
from .basic_model import BasicClass


class Camera(BasicClass):
   Etat = (('en service','en service'),
	('hors service','hors service')
   )
   
   description = models.TextField(null=False,unique=True)
   position = models.TextField(null=False)
   etat= models.CharField(max_length=20,choices=Etat,default='hors service')
