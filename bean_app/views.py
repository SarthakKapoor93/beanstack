from django.shortcuts import render
from django.http import HttpResponse
#This is a test comment

def home(request):
    return render(request, 'bean_app/Home.html', {})
