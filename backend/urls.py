from django.urls import path, include
from rest_framework import routers


urlpatterns = [ 
    path('api/', include('backend.api.url', namespace='api')),
]