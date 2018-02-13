from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from bean_app.models import CoffeeBean, Review, Vendor
import requests
from xml.etree import ElementTree


def home(request):
    # Return the top three beans
    beans = CoffeeBean.objects.order_by('average_rating')[:3]
    return render(request, 'bean_app/home.html', {'beans': beans})


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


def show_coffee_details(request, coffee_name_slug):

    bean = CoffeeBean.objects.get(slug=coffee_name_slug)
    context = {'bean': bean,
               'tags': bean.tags.all(),
               'reviews': Review.objects.filter(coffee_bean=bean)
               }
    return render(request, 'bean_app/bean_details.html', context)


def maps(request):

    positions = None

    # If they want to see all the beanstack cafes on the map
    beanstack_cafes = request.GET.get('beanstack-cafes', False)
    if beanstack_cafes:
        # Access the lat and long values from all cafes in the database
        positions = [{'lat': 55.8308988, 'lng': -4.0756677}, {'lat': 55.860081, 'lng': -4.254018}]

    # If they want to see a specific beanstack cafe on the map,
    # get the id from the request
    selected_cafe_id = request.GET.get('selected-cafe', None)
    selected_cafe = bool(selected_cafe_id)
    if selected_cafe_id:
        # retrieve the cafe from the database
        # cafe = Vendor.objects.get(pk=selected_cafe_id);
        # selected_cafe = {'lat': cafe.lat, 'lng': cafe.lng}

        positions = [{'lat': 55.8308988, 'lng': -4.0756677}]

    context = {
        'beanstack_cafes': beanstack_cafes,
        'selected_cafe': selected_cafe,
        'selected_cafe_id': selected_cafe_id,
        'other_cafes': request.GET.get('other-cafes', False),
        'positions': positions
    }
    return render(request, 'bean_app/maps.html', context)


# def get_nearby(request):
#     lat = request.GET['lat']
#     long = request.GET['long']
#
#     url = "https://maps.googleapis.com/maps/api/place/textsearch/xml?query=coffee+shops&radius=1000" \
#           "&location=" + lat + "," + long + " &key=AIzaSyAjPKmaEJcP6rXu-pud3Mfp-HbXekUm4Cw"
#
#     r = requests.get(url)
#     xml = r.text.encode('utf-8')
#     root = ElementTree.fromstring(xml)
#     lat = root[1].find('geometry').find('location').find('lat').text
#     long = root[1].find('geometry').find('location').find('lng').text
#
#     return HttpResponse({'lat': lat, 'long': long})









