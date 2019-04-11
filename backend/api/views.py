from django.shortcuts import render
from rest_framework import generics
from ..models import Product, Certificate, Service
from .serializers import productSerializer, certificateSerializer, serviceSerializer


# Create your views here.
class ProductListView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	
class CertificateListView(generics.ListAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer


class CertificateDetailView(generics.RetrieveAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

	
class ServiceListView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ServiceSerializer


class ServiceDetailView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ServiceSerializer
