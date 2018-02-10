from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from bean_app.models import CoffeeBean


def home(request):
    return render(request, 'bean_app/home.html', {})


def about(request):
    return render(request, 'bean_app/about.html', {})


def contact(request):
    return render(request, 'bean_app/contact.html', {})


def browse(request):
    beans = CoffeeBean.objects.all()
    return render(request, 'bean_app/browse.html', {'beans': beans})


def login(request):
    return render(request, 'bean_app/login.html', {})


def my_account(request):
    return render(request, 'bean_app/myaccount.html', {})


def signup(request):
    return render(request, 'bean_app/signup.html', {})


def addproduct(request):
    return render(request, 'bean_app/addproduct.html', {})



