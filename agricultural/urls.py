""" Default urlconf for agricultural """

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from agricultural import settings
admin.autodiscover()



def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agricultural.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
    url(r'^accounts/', include('allauth.urls')),
    url(r'', include('base.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

