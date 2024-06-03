from django.shortcuts import render
from django.http import HttpResponse  # This import may not be necessary for this particular view

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')
