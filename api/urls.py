"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls import include
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from django.conf.urls.static import static

import os

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Retrouvez la lien vers la vue par defaut des APIs
    """
    return Response({
            'MAIN APIs': "http://localhost:8080/main-api/",
        })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main-api/', include('main.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('', api_root)
]
# This is only needed when using runserver.
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)