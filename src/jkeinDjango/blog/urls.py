from django.conf.urls.defaults import patterns, include, url
from views import allitems, categoryview, articledetail
urlpatterns = patterns('',

url(r'^$', allitems),
url(r'^category/(?P<name_slug>.*)/$', categoryview),
url(r'^(?P<slug>.*)/', articledetail),
url(r'^comments/', include('django.contrib.comments.urls')),
)
