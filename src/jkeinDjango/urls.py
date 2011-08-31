from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jkeinDjango.views.home', name='home'),
    # url(r'^jkeinDjango/', include('jkeinDjango.foo.urls')),

url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
url(r'^admin/', include(admin.site.urls)),
url(r'^$', include('jkeinDjango.frontpage.urls')),
url(r'^blog/', include('jkeinDjango.blog.urls')),
url(r'^tinymce', include ('tinymce.urls')),
)

# DEV SERVER ONLY
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
            (r'^uploads/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )