from django.contrib import admin
from .models import Product, Certificate, Service


admin.site.register(Product)
admin.site.register(Certificate)
admin.site.register(Service)