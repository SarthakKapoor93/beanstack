from django.db import models
from django.contrib.auth.models import User


class CoffeeProduct(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1000, blank=True)
    origin = models.CharField(max_length=128)
    price = models.FloatField(default=None, blank=True, null=True)
    average_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    coffee_product = models.ForeignKey(CoffeeProduct)
    description = models.CharField(max_length=240)
    rating = models.IntegerField(default=0)
    reviewer = models.CharField(max_length=128)

    def __str__(self):
        return "Review of {} by {}".format(self.coffee_product, self.reviewer)


class UserAccount(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


'''
Remember to add new models to bean_app/admin.py
and to make migrations after making any changes 
to the models.
'''
