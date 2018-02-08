from django.conf.urls import url
from bean_app import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^login', views.login, name='login'),
    url(r'^myaccount', views.myaccount, name='myaccount'),
    url(r'^$', views.addproduct, name='addproduct'),
    url(r'^signup', views.signup, name='signup'),
]
