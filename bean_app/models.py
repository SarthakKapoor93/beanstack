from django.db import models
from django.contrib.auth.models import User

'''
    *** NOTES: ***
    - Remember to add new models to bean_app/admin.py
    and to make migrations after making any changes 
    to the models.
    - We may need to include slugs for some of the objects
'''


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "Tag: {} - {}".format(self.pk, self.name)


class CoffeeBean(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(blank=True)  # Just making this blank for testing
    location = models.CharField(max_length=128)   # This might need to be coordinates depending on the google maps api
    description = models.CharField(max_length=1000, blank=True)
    price = models.FloatField(default=None, blank=True, null=True)
    average_rating = models.FloatField(default=0)
    t_type = models.CharField(max_length=128, blank=True)  # what is type exactly? Need different name/ clashes with python built in type
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "Coffee bean: {} - {}".format(self.pk, self.name)


class Customer(models.Model):
    # We don't need a customer id number do? Just use to pk?
    fullname = models.CharField(max_length=128)
    email = models.EmailField()
    # password = models.CharField()   This would store the password as a string, Django handles this for us
    # address = models.CharField()      Do we need their address?
    # telephone = models.CharField()   Do we need the telephone?
    favourite_coffee = models.ForeignKey(CoffeeBean)
    # Makes more sense to have the link here, rather than the char field?

    def __str__(self):
        return "Customer: {} - {}".format(self.pk, self.fullname)


class Review(models.Model):
    customer = models.ForeignKey(Customer)
    coffee_bean = models.ForeignKey(CoffeeBean)
    # Don't need to use '_id' in the variable name. ORM allows us to just treat this as the object rather than a pk
    rating = models.IntegerField()  # Why float field? I just assumed we would be using a star system or something?
    comment = models.TextField(max_length=240, blank=True)

    def __str__(self):
        return "Review: {} of {} by {}".format(self.pk, self.coffee_bean, self.customer)


class Vendor(models.Model):
    owner_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    business_name = models.CharField(max_length=128, unique=True)
    # password = models.CharField()
    url_online_shop = models.URLField()
    address = models.CharField(max_length=128)
    # telephone = models.CharField()
    description = models.CharField(max_length=128, blank=True)
    products_in_stock = models.ManyToManyField(CoffeeBean)

    # This could be useful, if we can implement it
    # def has_online_shop(self):
    #     return True if url_online_shop exits

    def __str__(self):
        return "Vendor: {} - {} - {}".format(self.pk, self.owner_name, self.business_name)


class UserAccount(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username