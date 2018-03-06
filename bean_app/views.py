from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from bean_app.google_maps_api import Mapper
from django.core.paginator import Paginator
import json

from bean_app.models import CoffeeBean, Review, Vendor

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


# def login(request):
#   if request.method == 'POST':

#        username = request.POST.get('username')
#   password = request.POST.get('password')

#   user = authenticate(username=username, password=password)
#
#   if user:

#            if user.is_active:
#           login(request, user)
#           return HttpResponseRedirect(reverse('index'))
#       else:
#           return HttpResponse("Your beanstack account is disabled.")
#   else:
#       print("Invalid login details: {0}, {1}".format(username, password))
#       return HttpResponse("Invalid login details supplied.")
#
#
#    else:
#
#    return render(request, 'bean_app/login.html', {})
#


# def my_account(request):
#   my_account_complete = False

#    if request.method == 'POST':
#   my_account_form = MyAccountForm(data=request.POST)
#   account_form = AccountForm(data=request.POST)

#        if my_account_form.is_valid() and account_form.is_valid():

#       user = account_form.save()
#            user.save()

#       account = account_form.save(commit=False)
#       account.user = user

#       if 'picture' in request.FILES:
#           account.picture = request.FLIES['picture']
#       account.save()

#       my_account_complete = True
#   else:


#       print(my_account_form.errors, account_form.errors)
# else:
#   my_account_form = MyAccountForm()
#   account_form = AccountForm()

#     if 'picture' in request.FILES:
#           account.picture = request.FILES['picture']
#        account.save()


#    return render(request, 'bean_app/myaccount.html', {
#   'MyAccountForm': my_account_form,
#   'AccountForm': account_form,
#   'my_account_complete': my_account_complete})

#
# def signup(request):
#   signup_complete = False

#    if request.method == 'POST':
#   signup_form = SignupForm(data=request.POST)

#        print(type(signup_form))


#        if signup_form.is_valid():

#       user = signup_form.save()
#       user.save()

#            account = signup_form.save(commit=False)
#       account.user = user

#            signup_complete = True
#   else:

#       print("!!!!!!!!!!!!!", signup_form.errors)
# else:
#   signup_form = SignupForm()

#    return render(request, 'bean_app/signup.html', {
#   'SignupForm': signup_form,
#   'signup_complete': signup_complete})

#    return render(request, 'bean_app/registration_form.html', {
#        'SignupForm': signup_form,
#       'AccountForm': account_form,
#       'signup_complete': signup_complete})



def addproduct(request):
    return render(request, 'bean_app/addproduct.html', {})


def signupselection(request):
    return render(request, 'bean_app/signupselection.html', {})


# def vendorsignup(request):
#   vendor_signup_complete = False

#    if request.method == 'POST':
#   vendor_signup_form = VendorSignupForm(data=request.POST)
#   vendor_account_form = VendorAccountForm(data=request.POST)

#        if vendor_signup_form.is_valid():

#            user = vendor_account_form.save()
##       user.set_password(user.password)
#      user.save()

#       account = vendor_account_form.save(commit=False)
#       account.user = user

#            if 'picture' in request.FILES:
#           account.picture = request.FLIES['picture']
#       account.save()

#       vendor_signup_complete = True


#   else:
#       print(vendor_signup_form.errors, vendor_account_form.errors)


#    else:
#   vendor_signup_form = VendorSignupForm()
#   vendor_account_form = VendorAccountForm()

#    return render(request, 'bean_app/vendorsignup.html', {
#   'vendor_signup_form': vendor_signup_form,
#   'vendor_account_form': vendor_account_form,
#   'vendor_signup_complete': vendor_signup_complete})


def product(request, coffee_name_slug):

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


        #        if user:
        #       if user.is_active:
        #           login(request, user)
        #           return HttpResponseRedirect(reverse('index'))
        #       else:
        #           return HttpResponse("Please create a Beanstack account. Your credentials does not exits.")
        #   else:
        #       print("Invalid login details: {0}, {1}".format(username, password))
        #       return HttpResponse("Invalid login details supplied.")
        # else:


#   return render(request, 'bean_app/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can't view this site!")


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


def social_djangomysite(request):
    return render(request, 'bean_app/login.html', {})


def mysite(request):
    return render(request, 'bean_app/login.html', {})


def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")
