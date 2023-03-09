from django.db import models
from .basic_model import BasicClass


class Category(BasicClass):
   name = models.TextField(null=False)
   description = models.TextField(null=False,unique=True)
