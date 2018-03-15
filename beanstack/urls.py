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
    # we need to do this to make sure there is a user profile
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
    url(r'^bean_app/', include('bean_app.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

