from django.db import models
from .basic_model import BasicClass
from .plot_model import Plot
from datetime import datetime
from .customer_model import Customer


def getCurrentMonth():
    today=datetime.now()
    return today.strftime("%b")


class Report(BasicClass):
   '''plot model'''
   MONTH = (('January','January'),('Febuary','Febuary'),('March','March'),
           ('April','April'),('May','May'),('June','June'),('July','July'),
           ('August','August'),('September','September'),('October','October'),
           ('November','November'),('December','December')
   )
   TYPE = (('Tomatoes','Tomatoes'),('Onions','Onions'),('Cabbage','Cabbage'),('Carrots','Carrots'))
   
   crop_type = models.CharField(max_length=20,choices=TYPE,default='Cabbage')
   month = models.CharField(max_length=20,choices=MONTH,default=str(getCurrentMonth()))
   plot = models.ForeignKey(Plot,on_delete=models.PROTECT,verbose_name='land')
   operator=models.ForeignKey(Customer,on_delete=models.PROTECT,verbose_name='operator')
   income=models.PositiveIntegerField(default=0)
