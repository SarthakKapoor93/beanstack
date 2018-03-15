from django import forms
from bean_app.models import Vendor


class VendorForm(forms.ModelForm):
    owner_name = forms.CharField(max_length=128)
    email = forms.EmailField()
    business_name = forms.CharField(max_length=128)
    url_online_shop = forms.URLField()
    address = forms.CharField(max_length=128)
    description = forms.CharField(max_length=1000)
    products_in_stock = forms.SelectMultiple()

    class Meta:
        model = Vendor
        fields = ('owner_name', 'email', 'business_name', 'url_online_shop', 'address', 'description', 'products_in_stock')

