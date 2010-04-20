from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Post, Link

urlpatterns = patterns('',
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/js'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/css'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/images'}),
    # Example:
    # (r'^simpleblog/', include('simpleblog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'blog.views.post_index'),
    url(r'^post/(?P<post_id>\d+)/$', 'blog.views.post_show', name='post-show'),
    url(r'^links', 'blog.views.link_index', name='link-index'),
)
