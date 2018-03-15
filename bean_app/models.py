from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from bean_app.google_maps_api import Mapper

'''
    *** NOTES: ***
    - Remember to add new models to bean_app/admin.py
    and to make migrations after making any changes 
    to the models.
    - We may need to include slugs for some of the objects
'''

mapper = Mapper()


class TagType(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "Tag Type: {} pk: {}".format(self.name, self.pk)


class Tag(models.Model):
    tag_type = models.ForeignKey(TagType, blank=True, default=None)
    value = models.IntegerField(default=0)
    coffee_bean = models.ForeignKey('CoffeeBean', default=None,
                                    blank=True, related_name='tags')

    def __str__(self):
        return "{}".format(self.tag_type.name)


class CoffeeBean(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(blank=True)
    location = models.CharField(max_length=128)
    description = models.CharField(max_length=1000, blank=True)
    price = models.FloatField(default=None, blank=True, null=True)
    average_rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CoffeeBean, self).save(*args, **kwargs)

    class Meta:
        ordering = ('average_rating',)

    def __str__(self):
        return "Coffee bean: {} - {}".format(self.pk, self.name)


class UserProfile(models.Model):
    """
    This model is combined with and extends the functionality
    of the Django user model. It adds the ability to save coffees
    to a user.
    """
    user = models.OneToOneField(User)
    saved_coffees = models.ManyToManyField(CoffeeBean, blank=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    user = models.ForeignKey(User, blank=True, default=None)
    coffee_bean = models.ForeignKey(CoffeeBean)
    rating = models.IntegerField()
    comment = models.TextField(max_length=240, blank=True)

    def __str__(self):
        return "Review: {} of {} by {}".format(self.pk, self.coffee_bean, self.user)


class Vendor(models.Model):
    owner_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    business_name = models.CharField(max_length=128, unique=True)
    url_online_shop = models.URLField(blank=True)
    address = models.CharField(max_length=128)
    description = models.TextField(max_length=1000, blank=True)
    products_in_stock = models.ManyToManyField(CoffeeBean)
    lat = models.FloatField(default=None, blank=True)
    long = models.FloatField(default=None, blank=True)

    def save(self, *args, **kwargs):
        """
        Before saving the vendor, do the geolocation
        """
        data = mapper.geocode(address=self.address)
        self.address, self.lat, self.long = data
        super(Vendor, self).save(*args, **kwargs)

    def __str__(self):
        return "Vendor: {} - {} - {}".format(self.pk, self.owner_name, self.business_name)

