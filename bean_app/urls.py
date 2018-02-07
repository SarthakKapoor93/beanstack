from django.conf.urls import url
from bean_app import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^contact',views.contact, name='contact')
]
