from django.conf.urls import url
from bean_app import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^login', views.login, name='login'),
    url(r'^myaccount', views.my_account, name='my_account'),
    url(r'^addproduct', views.addproduct, name='addproduct'),
    url(r'^product/(?P<coffee_name_slug>[\w\-]+)/$', views.product, name='product'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^vendorsignup', views.signup, name='vendorsignup'),
    url(r'^signupselection', views.signupselection, name='signupselection'),
    url(r'^maps$', views.maps, name='maps'),
    url(r'^load_api', views.load_api, name='load_api'),
    url(r'^cafes$', views.get_beanstack_cafes, name="get_cafes"),
    ]


