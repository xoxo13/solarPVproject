from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('policy/', views.policy, name='policy'),
    path('registration/', views.registration, name='registration'),
    path('wpdash/', views.wpdash, name='wpdash')
     path('testcert/', views.testcert, name='testcert')
]