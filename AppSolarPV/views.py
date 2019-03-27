from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'AppSolarPV/index.html')
	
def contact(request):
	return render(request, 'AppSolarPV/contact.html')
	
def login(request):
	return render(request, 'AppSolarPV/login.html')
	
def policy(request):
	return render(request, 'AppSolarPV/policy.html')
	
def registration(request):
	return render(request, 'AppSolarPV/registration.html')
	
def wpdash(request):
	return render(request, 'AppSolarPV/wpdash.html')