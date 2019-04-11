from django.contrib import admin
from .models import Product, Certificate, Service


# Register your models here.
admin.site.register(Product)

admin.site.register(Certificate)

admin.site.register(Service)