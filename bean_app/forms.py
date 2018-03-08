from django import forms
from django.contrib.auth.models import User
from bean_app.models import Tag, CoffeeBean, Review, Vendor


class Tag(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Tag name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Tag
        fields = ('name',)


class CoffeeBean(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the Coffee Bean title.")
    url = forms.CharField(max_length=200,
                          help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = CoffeeBean
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data


# class Customer(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ('',)


# class Review(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ('',)


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


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#
# class UserAccount(forms.ModelForm):
#     class Meta:
#         model = UserAccount
#         fields = ('website', 'picture')
