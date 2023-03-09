#from expense.view.ligne_expense_view import get_ligne_expense
from django.urls import path
from . import views
from django.conf.urls import include

from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'customers', views.CustomerViewSet)
routers.register(r'plots', views.PlotViewSet)
routers.register(r'reports', views.ReportViewSet)
routers.register(r'category', views.CategoryViewSet)
routers.register(r'camera', views.CameraViewSet)
routers.register(r'detection', views.DetectionViewSet)
routers.register(r'alerte', views.AlerteViewSet)

urlpatterns = [
    path('', include(routers.urls)),   
    path('login/', views.login),

]
#path('update-ligne/<str:id>/', views.update_ligne_expense),
#path('create-ligne/', views.create_ligne_expense),
