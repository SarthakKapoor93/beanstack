"""beanstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from bean_app import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^$', views.about, name='about'),
    url(r'^$', views.contact, name='contact'),
    url(r'^$', views.browse, name='browse'),
    url(r'^$', views.login, name='login'),
    url(r'^$', views.myaccount, name='myaccount'),
    url(r'^$', views.signup, name='signup'),
    url(r'^$', views.vendorsignup, name='vendorsignup'),
    url(r'^$', views.addproduct, name='addproduct'),
    url(r'^$', views.signupselection, name='signupselection'),
    url(r'^$', views.product, name='product'),
    url(r'^bean_app/', include('bean_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
