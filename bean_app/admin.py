from django.contrib import admin
import bean_app.models


class CoffeeBeanAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(bean_app.models.Tag)
admin.site.register(bean_app.models.CoffeeBean)
admin.site.register(bean_app.models.Customer)
admin.site.register(bean_app.models.Review)
admin.site.register(bean_app.models.Vendor)
# admin.site.register(bean_app.models.AccountForm)
# admin.site.register(bean_app.models.VendorAccountForm)
# admin.site.register(bean_app.models.VendorSignupForm)
# admin.site.register(bean_app.models.SignupForm)
admin.site.register(bean_app.models.social_djangomysite)
admin.site.register(bean_app.models.mysite)

