from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Report)
admin.site.register(Customer)
admin.site.register(Plot)
admin.site.register(Camera)
admin.site.register(Alerte)
admin.site.register(Detection)
admin.site.register(Category)
