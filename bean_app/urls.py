from django.conf.urls import url
from bean_app import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
]
