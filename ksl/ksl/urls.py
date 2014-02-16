from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ksl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('core.urls')),
)

