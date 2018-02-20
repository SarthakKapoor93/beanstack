from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from bean_app.models import CoffeeBean, Review, Vendor
from bean_app.google_maps_api import Mapper
import json

mapper = Mapper()


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


def signupselection(request):
    return render(request, 'bean_app/signupselection.html', {})


def vendorsignup(request):
    return render(request, 'bean_app/vendorsignup.html', {})

'''
The product method should also return a list of the coffee shops that 
sell this product. Then you don't need to do another ajax call for it.

'''


def product(request, coffee_name_slug):

    bean = CoffeeBean.objects.get(slug=coffee_name_slug)
    context = {'bean': bean,
               'tags': bean.tags.all(),
               'reviews': Review.objects.filter(coffee_bean=bean)
               }
    return render(request, 'bean_app/product.html', context)


def maps(request):
#
#     positions = None
#
#     # If they want to see all the beanstack cafes on the map
#     beanstack_cafes = request.GET.get('beanstack-cafes', False)
#     if beanstack_cafes:
#         # Access the lat and long values from all cafes in the database
#         positions = [{'lat': vendor.lat, 'lng': vendor.long} for vendor in Vendor.objects.all()]
#
#     # If they want to see a specific beanstack cafe on the map,
#     # get the id from the request
#     selected_cafe_id = request.GET.get('selected-cafe', None)
#     selected_cafe = bool(selected_cafe_id)
#     if selected_cafe_id:
#         # retrieve the cafe from the database
#         cafe = Vendor.objects.get(pk=selected_cafe_id)
#         positions = [{'lat': cafe.lat, 'lng': cafe.long}]
#
#     context = {
#         'beanstack_cafes': beanstack_cafes,
#         'selected_cafe': selected_cafe,
#         'selected_cafe_id': selected_cafe_id,
#         'other_cafes': request.GET.get('other-cafes', False),
#         'positions': positions
#     }
    return render(request, 'bean_app/maps.html', {})


def load_api(request):
    """
    Takes makes a call to the mapper object in order
    to retrieve javascript from the api.
    :param request:
    :return:
    """
    return HttpResponse(mapper.get_javascript())


def get_beanstack_cafes(request):
    """
    Checks if there is a coffee_id
    :param request:
    :return:
    """

    coffee_id = request.GET.get('coffee_id', None)
    if coffee_id:
        vendors = []
        for vendor in Vendor.objects.all():
            coffee = vendor.products_in_stock.filter(pk=coffee_id).first()
            if coffee:
                vendors.append(vendor)
    else:
        vendors = Vendor.objects.all()
    positions = [{"lat": vendor.lat, "lng": vendor.long} for vendor in vendors]
    return HttpResponse(json.dumps(positions))
