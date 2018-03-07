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
from bean_app.models import UserProfile
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/bean_app/home/'

    # This function overrides the django-redux function
    # we need to do this to make sure that the user profile
    # associated with a user
    def register(self, form):
        if form.is_valid():
            user = form.save()
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            return user


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    # url(r'^$', views.about, name='about'),
    # url(r'^$', views.contact, name='contact'),
    # url(r'^$', views.browse, name='browse'),
    # url(r'^$', views.login, name='login'),
    # url(r'^$', views.my_account, name='myaccount'),
    # url(r'^$', views.signup, name='signup'),
    # url(r'^$', views.vendorsignup, name='vendorsignup'),
    # url(r'^$', views.addproduct, name='addproduct'),
    # url(r'^$', views.signupselection, name='signupselection'),
    # url(r'^$', views.product, name='product'),

    url(r'^bean_app/', include('bean_app.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

