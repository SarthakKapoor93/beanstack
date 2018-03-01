from django.contrib import admin
from bean_app.models import *


class CoffeeBeanAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag)
admin.site.register(TagType)
admin.site.register(CoffeeBean)
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Vendor)
admin.site.register(AccountForm)
admin.site.register(VendorAccountForm)
admin.site.register(VendorSignupForm)
admin.site.register(SignupForm)