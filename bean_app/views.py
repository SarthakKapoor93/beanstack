from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from bean_app.models import *
from bean_app.google_maps_api import Mapper
from bean_app.forms import VendorForm
from django.core.paginator import Paginator

from django.db.models import Q

import json

mapper = Mapper()


def home(request):
    # Return the top three beans
    beans = CoffeeBean.objects.order_by('average_rating')[:3]
    return render(request, 'bean_app/home.html', {'beans': beans})


def about(request):
    return render(request, 'bean_app/about.html', {})


def brewing(request):
    context = {
        'brewing_guides': BrewingGuide.objects.all()
    }
    return render(request, 'bean_app/brewing.html', context=context)


def brewing_details(request, brewing_guide_slug):
    context = {
        'guide': BrewingGuide.objects.get(slug=brewing_guide_slug)
    }
    return render(request, 'bean_app/brewing_details.html', context=context)


def browse(request):
    # Get all the beans from the database ordered by the rating
    beans = CoffeeBean.objects.order_by('-average_rating')

    #  Pagination
    page_number = request.GET.get('page', 1)
    paginator = Paginator(beans, 5, orphans=2)
    page = paginator.page(page_number)

    context = {
        "beans": page,
        'len_results': len(beans)
    }
    return render(request, 'bean_app/browse.html', context)


def build_query(query_terms):
    query = Q(name__icontains=query_terms[0])
    for term in query_terms[1:]:
        query = query | Q(name__icontains=term)
    return query


def search(request):

    query = request.GET.get('q').strip()
    # Check if an empty string was entered
    if query:
        query_terms = query.split()

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
    else:
        # If an empty string was entered return all results
        results = CoffeeBean.objects.order_by('-average_rating')
        query = None

    # Pagination
    page_number = request.GET.get('page', 1)
    paginator = Paginator(list(results), 5, orphans=2)
    page = paginator.page(page_number)

    context = {'beans': page,
               'search_term': query,
               'len_results': len(results)
               }

    return render(request, 'bean_app/browse.html', context)


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
        context = {
            'bean_data': bean_data,
            'vendorsignup': True,
        }
        return render(request, 'bean_app/vendorsignup.html', context)


def product(request, coffee_name_slug):

    # If the user is posting a review
    if request.method == 'POST':
        has_posted = True

        user = request.user
        comment = request.POST.get('comment')
        coffee_bean_slug = request.POST.get('coffee-bean')
        rating = request.POST.get('rating', 0)
        coffee_bean = CoffeeBean.objects.get(slug=coffee_bean_slug)

        # Make sure that the user hasn't already left a review for this coffee
        reviews = Review.objects.filter(user=user, coffee_bean=coffee_bean)
        if reviews:
            successful_review = False
        else:
            successful_review = True

            # Create the review
            review = Review(user=user,
                            comment=comment,
                            coffee_bean=coffee_bean,
                            rating=rating
                            )
            review.save()

            # Update the tags with the values from the post data
            tag_types = TagType.objects.all()
            # Loop over the tag types and use the name to get the values from the post
            for tag_type in tag_types:
                value = request.POST.get(tag_type.name)
                if value:
                    tag = Tag.objects.filter(tag_type=tag_type, coffee_bean=coffee_bean).first()
                    # Update the tag value
                    if value == '+':
                        tag.value += 1
                    elif value == '-':
                        tag.value -= 1

                    tag.save()

    else:
        # Otherwise - The user has made a get request
        has_posted = False
        successful_review = False

    saved_coffees = []
    if request.user.is_authenticated():
        # Use get or create because we can't be sure that the users who have logged in via facebook have a user profile
        profile = UserProfile.objects.get_or_create(user=request.user)[0]
        coffees = list(profile.saved_coffees.all())
        saved_coffees = [(coffees.index(bean) + 2, bean) for bean in coffees]

    # This boolean flag controls some javascript that automatically scrolls
    # to the reviews section on page load
    display_reviews = bool(request.GET.get('reviews', False))

    coffee_bean = CoffeeBean.objects.get(slug=coffee_name_slug)
    context = {'bean': coffee_bean,
               'tags': coffee_bean.tags.order_by('value')[::-1],
               'reviews': Review.objects.filter(coffee_bean=coffee_bean),
               'display_reviews': display_reviews,
               'saved_coffees': saved_coffees,
               'has_posted': has_posted,
               'successful_review': successful_review,
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


@login_required
def update_my_beanstack(request):
    # Take the bean slug from the get request
    bean_slug = request.GET.get('bean_slug', None)
    bean = CoffeeBean.objects.get(slug=bean_slug)

    # Get the user profile for the current user and add the bean
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    user_profile.saved_coffees.add(bean)
    return HttpResponse()


@login_required
def my_beanstack(request):
    # Get the user profile for the user
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    coffees = list(profile.saved_coffees.all())
    saved_coffees = [(coffees.index(bean) + 2, bean) for bean in coffees]

    return render(request, 'bean_app/mybeanstack.html', {'saved_coffees': saved_coffees})


# Don't know how to override the change password part of django auth
# Do an ajax call from the account page to access the user's saved coffees
@login_required
def get_saved_coffees(request):
    profile = UserProfile.objects.get_or_create(user=request.user)[0]

    data = []
    for coffee in profile.saved_coffees.all():
        coffee_data = {'name': coffee.name,
                       'slug': coffee.slug}
        data.append(coffee_data)

    return HttpResponse(json.dumps(data))
