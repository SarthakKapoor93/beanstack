from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'bean_app/Home.html', {})


def about(request):
    return render(request, 'bean_app/about.html', {})


def contact(request):
    return render(request, 'bean_app/contact.html', {})


def browse(request):
    return render(request, 'bean_app/browse.html', {})


def login(request):
    return render(request, 'bean_app/login.html', {})


def my_account(request):
    return render(request, 'bean_app/myaccount.html', {})


def signup(request):
    return render(request, 'bean_app/signup.html', {})


def addproduct(request):
    return render(request, 'bean_app/addproduct.html', {})



