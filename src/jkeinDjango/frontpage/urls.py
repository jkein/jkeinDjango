from django.conf.urls.defaults import patterns, include, url
from views import frontpage

urlpatterns = patterns('',

url(r'^$', frontpage),
)