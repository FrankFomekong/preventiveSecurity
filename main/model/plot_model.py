from django.db import models
from .basic_model import BasicClass
from .customer_model import Customer

class Plot(BasicClass):
   '''plot model'''
   name = models.TextField(null=False)
   location = models.TextField(null=False)
   area = models.TextField(null=False)
   photo = models.ImageField(upload_to="img/plots/",blank=True,verbose_name="Image")
   owner = models.ForeignKey(Customer,on_delete=models.PROTECT,verbose_name='owner')
