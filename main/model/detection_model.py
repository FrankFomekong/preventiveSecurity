from django.db import models
from .basic_model import BasicClass


class Detection(BasicClass):
   TYPE = (('iconnu','inconnu'),
	('operator','operator')
   )
   
   idPersonne = models.TextField(null=False)
   status = models.TextField(null=False)
   
