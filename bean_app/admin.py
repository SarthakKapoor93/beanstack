from django.contrib import admin
from bean_app.models import Tag, CoffeeBean, Customer, Review, Vendor, UserAccount


class CoffeeBeanAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Tag)
admin.site.register(CoffeeBean)
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Vendor)
admin.site.register(UserAccount)

