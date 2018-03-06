from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from bean_app.models import CoffeeBean, Review, Vendor, VendorAccountForm, VendorSignupForm, AccountForm, SignupForm, Tag, UserProfile, User
from bean_app.google_maps_api import Mapper
from bean_app.forms import VendorForm
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

    # Filter by the tags and then get all the coffees associated with each tag
    tag_matches = set()
    for tag in Tag.objects.filter(build_query(query_terms)):
        beans = tag.coffee_beans.all()
        tag_matches |= set(beans)

    results = name_matches | tag_matches
    context = {'beans': results}

    return render(request, 'bean_app/search.html', context)


def login(request):
    return render(request, 'bean_app/login.html', {})


def my_account(request):
    return render(request, 'bean_app/myaccount.html', {})


def signup(request):
    signup_complete = False

    if request.method == 'POST':
        signup_form = SignupForm(data=request.POST)
        account_form = AccountForm(data=request.POST)

        if signup_form.is_valid() and account_form.is_valid():

            user = account_form.save()
            user.set_password(user.password)
            user.save()

            account = account_form.save(commit=False)
            account.user = user

            if 'picture' in request.FILES:
                account.picture = request.FILES['picture']
            account.save()

            signup_complete = True
        else:

            print(signup_form.errors, account_form.errors)
    else:
        signup_form = SignupForm()
        account_form = AccountForm()

    return render(request, 'bean_app/registration_form.html', {
        'SignupForm': signup_form,
        'AccountForm': account_form,
        'signup_complete': signup_complete})


def addproduct(request):
    return render(request, 'bean_app/addproduct.html', {})


def signupselection(request):
    return render(request, 'bean_app/signupselection.html', {})


def vendor_signup(request):

    if request.method == 'POST':
        form = VendorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'bean_app/home.html', {})
        else:
            print(form.errors)
    else:
        # Get the list of coffee shops and pks to display in the menu
        bean_data = [(bean.pk, bean.name) for bean in CoffeeBean.objects.all()]
        return render(request, 'bean_app/vendorsignup.html', {'bean_data': bean_data})


# def vendorsignup(request):
#     vendor_signup_complete = False
#
#     if request.method == 'POST':
#         vendor_signup_form = VendorSignupForm(data=request.POST)
#         vendor_account_form = VendorAccountForm(data=request.POST)
#
#         if vendor_signup_form.is_valid():
#
#             user = vendor_account_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             account = vendor_account_form.save(commit=False)
#             account.user = user
#
#             if 'picture' in request.FILES:
#                 account.picture = request.FLIES['picture']
#             account.save()
#
#             vendor_signup_complete = True
#
#         else:
#             print(vendor_signup_form.errors, vendor_account_form.errors)
#
#     else:
#         vendor_signup_form = VendorSignupForm()
#         vendor_account_form = VendorAccountForm()
#
#     return render(request, 'bean_app/vendorsignup.html', {
#         'vendor_signup_form': vendor_signup_form,
#         'vendor_account_form': vendor_account_form,
#         'vendor_signup_complete': vendor_signup_complete})


def product(request, coffee_name_slug):

    bean = CoffeeBean.objects.get(slug=coffee_name_slug)

    # This view also needs to pass back the users, saved coffees in the context
    # (we could also do this via an ajax request)
    profile = UserProfile.objects.get(user=request.user)

    coffees = list(profile.saved_coffees.all())
    saved_coffees = [(coffees.index(bean) + 2, bean) for bean in coffees]

    context = {'bean': bean,
               'tags': bean.tags.all(),
               'reviews': Review.objects.filter(coffee_bean=bean),
               'saved_coffees': saved_coffees
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


# This might need to check if the coffee is already on the saved coffees list and let them know
def update_my_beanstack(request):
    # Take the bean slug from the get request
    bean_slug = request.GET.get('bean_slug', None)
    bean = CoffeeBean.objects.get(slug=bean_slug)

    # Get the user profile for the current user and add the bean
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.saved_coffees.add(bean)
    return HttpResponse()


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Please create a Beanstack account. Your credentials does not exits.")
#         else:
#             print("Invalid login details: {0}, {1}".format(username, password))
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render(request, 'bean_app/login.html', {})


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


def my_beanstack(request):
    # Get the user profile for the user
    profile = UserProfile.objects.get(user=request.user)
    saved_coffees = profile.saved_coffees.all()


    return render(request, 'bean_app/mybeanstack.html', {'saved_coffees': saved_coffees})
