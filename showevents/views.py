from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'showevents/templates/showevents/home.html', {'name': 'sina'})