from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from bean_app.models import CoffeeBean, Review, Vendor, VendorAccountForm, VendorSignupForm, AccountForm, MyAccountForm, SignupForm, \
    social_djangomysite
from bean_app.google_maps_api import Mapper

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
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your beanstack account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'bean_app/login.html', {})
    return render(request, 'bean_app/login.html', {})


def my_account(request):
    my_account_complete = False

    if request.method == 'POST':
        my_account_form = MyAccountForm(data=request.POST)
        account_form = AccountForm(data=request.POST)

        if my_account_form.is_valid() and account_form.is_valid():

            user = account_form.save()
            user.save()

            account = account_form.save(commit=False)
            account.user = user

            if 'picture' in request.FILES:
                account.picture = request.FLIES['picture']
            account.save()

            my_account_complete = True
        else:

            print(my_account_form.errors, account_form.errors)
    else:
        my_account_form = MyAccountForm()
        account_form = AccountForm()

    return render(request, 'bean_app/myaccount.html', {
        'MyAccountForm': my_account_form,
        'AccountForm': account_form,
        'my_account_complete': my_account_complete})


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
                account.picture = request.FLIES['picture']
            account.save()

            signup_complete = True
        else:

            print(signup_form.errors, account_form.errors)
    else:
        signup_form = SignupForm()
        account_form = AccountForm()

    return render(request, 'bean_app/signup.html', {
        'SignupForm': signup_form,
        'AccountForm': account_form,
        'signup_complete': signup_complete})


def addproduct(request):
    return render(request, 'bean_app/addproduct.html', {})


def signupselection(request):
    return render(request, 'bean_app/signupselection.html', {})


def vendorsignup(request):
    vendor_signup_complete = False

    if request.method == 'POST':
        vendor_signup_form = VendorSignupForm(data=request.POST)
        vendor_account_form = VendorAccountForm(data=request.POST)

        if vendor_signup_form.is_valid():

            user = vendor_account_form.save()
            user.set_password(user.password)
            user.save()

            account = vendor_account_form.save(commit=False)
            account.user = user

            if 'picture' in request.FILES:
                account.picture = request.FLIES['picture']
            account.save()

            vendor_signup_complete = True

        else:
            print(vendor_signup_form.errors, vendor_account_form.errors)

    else:
        vendor_signup_form = VendorSignupForm()
        vendor_account_form = VendorAccountForm()

    return render(request, 'bean_app/vendorsignup.html', {
        'vendor_signup_form': vendor_signup_form,
        'vendor_account_form': vendor_account_form,
        'vendor_signup_complete': vendor_signup_complete})


def product(request, coffee_name_slug):
    bean = CoffeeBean.objects.get(slug=coffee_name_slug)
    context = {'bean': bean,
               'tags': bean.tags.all(),
               'reviews': Review.objects.filter(coffee_bean=bean)
               }
    return render(request, 'bean_app/product.html', context)


def maps(request):
    positions = None

    # If they want to see all the beanstack cafes on the map
    beanstack_cafes = request.GET.get('beanstack-cafes', False)
    if beanstack_cafes:
        # Access the lat and long values from all cafes in the database
        positions = [{'lat': vendor.lat, 'lng': vendor.long} for vendor in Vendor.objects.all()]

    # If they want to see a specific beanstack cafe on the map,
    # get the id from the request
    selected_cafe_id = request.GET.get('selected-cafe', None)
    selected_cafe = bool(selected_cafe_id)
    if selected_cafe_id:
        # retrieve the cafe from the database
        cafe = Vendor.objects.get(pk=selected_cafe_id)
        positions = [{'lat': cafe.lat, 'lng': cafe.long}]

    context = {
        'beanstack_cafes': beanstack_cafes,
        'selected_cafe': selected_cafe,
        'selected_cafe_id': selected_cafe_id,
        'other_cafes': request.GET.get('other-cafes', False),
        'positions': positions
    }
    return render(request, 'bean_app/maps.html', context)


def load_api(request):
    """
    Takes makes a call to the mapper object in order
    to retrieve javascript from the api.
    :param request:
    :return:
    """
    return HttpResponse(mapper.get_javascript())


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
