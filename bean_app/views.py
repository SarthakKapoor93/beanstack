from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from bean_app.models import *
from bean_app.google_maps_api import Mapper
from django.core.paginator import Paginator

from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response
from functools import reduce
import operator
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
    # Get all the beans from the database ordered by the rating
    beans = CoffeeBean.objects.order_by('-average_rating')

    #  Pagination
    page_number = request.GET.get('page', 1)
    paginator = Paginator(beans, 5, orphans=2)
    page = paginator.page(page_number)

    context = {
        "beans": page
    }
    return render(request, 'bean_app/browse.html', context)


# def search(request):
#     beans = CoffeeBean.objects.order_by('-average_rating')
#
#     query = request.GET.get('q')
#     if query == " ":
#         beans = CoffeeBean.objects.order_by('-average_rating')
#     elif query:
#         query_list = query.split()
#         beans = beans.filter(
#             reduce(operator.and_, (Q(name__icontains=q) for q in query_list)) |
# 			reduce(operator.and_, (Q(location__icontains=q) for q in query_list))
#         )
#     else:
#          beans = CoffeeBean.objects.order_by('-average_rating')
#
#
# 	#  Pagination
#     page_number = request.GET.get('page', 1)
#     paginator = Paginator(beans, 5, orphans=2)
#     page = paginator.page(page_number)
#
#     context = {
#         "beans": page
#     }
#
#
#     return render(request, 'bean_app/search.html', context)


def build_query(query_terms):
    query = Q(name__icontains=query_terms[0])
    for term in query_terms[1:]:
        query = query | Q(name__icontains=term)
    return query


def search(request):

    query_terms = request.GET.get('q').split()

    # Filter by name or location of the coffee beans
    name_matches = set()
    for term in query_terms:
        beans = CoffeeBean.objects.filter(Q(name__icontains=term) | Q(location__icontains=term))
        name_matches |= set(beans)

    # Filter the tag types by the query terms
    tag_matches = set()
    for tag_type in TagType.objects.filter(build_query(query_terms)):

        # Use the tag type to get the tags for each of the types
        for tag in Tag.objects.filter(tag_type=tag_type):
            # Iterate over the tags and put the coffee objects into the result set
            tag_matches.add(tag.coffee_bean)

    results = name_matches | tag_matches
    context = {'beans': results}

    return render(request, 'bean_app/search.html', context)


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


def radar(request):

    # For the sake of testing, this view should get the first coffee and return the data
    bean = CoffeeBean.objects.get(pk=5)
    context = {'bean': bean,
               'tags': bean.tags.all(),
            }

    return render(request, 'bean_app/radar-chart.html', context=context)

'''
The product method should also return a list of the coffee shops that 
sell this product. Then you don't need to do another ajax call for it.

'''


def product(request, coffee_name_slug):

    # If the user is posting a review
    if request.method == 'POST':

        # Just take any customer for the time being
        customer = Customer.objects.all().first()
        comment = request.POST.get('comment')
        coffee_bean = request.POST.get('coffee-bean')
        rating = request.POST.get('rating')

        review = Review(customer=customer,
                        comment=comment,
                        coffee_bean=CoffeeBean.objects.get(slug=coffee_bean),
                        rating=rating)
        print(review)
        review.save()



    # Or they just want the details page

    bean = CoffeeBean.objects.get(slug=coffee_name_slug)
    context = {'bean': bean,
               'tags': bean.tags.all(),
               'reviews': Review.objects.filter(coffee_bean=bean)
               }
    return render(request, 'bean_app/product.html', context)


def load_api(request):
    """
    Makes a call to the mapper object in order
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

    # Get either the selected vendor objects
    coffee_id = request.GET.get('coffee_id', None)
    if coffee_id:
        vendors = []
        for vendor in Vendor.objects.all():
            coffee = vendor.products_in_stock.filter(pk=coffee_id).first()
            if coffee:
                vendors.append(vendor)
    else:
        # Or all of the vendor objects
        vendors = Vendor.objects.all()

    data = []
    # Arrange the vendor information
    for vendor in vendors:
        vendor_data = {"business_name": vendor.business_name,
                       "description": vendor.description,
                       "online-shop": vendor.url_online_shop,
                       "address": vendor.address,
                       "products": [coffee_bean.name for coffee_bean in vendor.products_in_stock.all()],
                       "lat": vendor.lat,
                       "lng": vendor.long
                       }
        data.append(vendor_data)
    return HttpResponse(json.dumps(data))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Please create a Beanstack account. Your credentials does not exits.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'bean_app/login.html', {})


@login_required
def restricted(request):
    return render(request, 'bean_app/restricted.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val
