from django.conf.urls import url
from bean_app import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^login', views.login, name='login'),
    url(r'^myaccount', views.my_account, name='my_account'),
    url(r'^$', views.addproduct, name='addproduct'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^showdetails/(?P<coffee_name_slug>[\w\-]+)/$', views.show_coffee_details, name='show_details'),
    url(r'^maps', views.maps, name='maps'),
    ]

