from django.db import models
from .basic_model import BasicClass


class Alerte(BasicClass):
   
   message= models.TextField(null=False)
   photo = models.ImageField(upload_to="img/plots/",blank=True,verbose_name="Image")
   id_detection=models.TextField(null=True)
