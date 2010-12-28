from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^parts_db/', include('parts_db.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    
    ('^parts/$', 'parts.views.index'),
    ('^parts/orders$', 'parts.views.list_orders'),
    ('^parts/parts$', 'parts.views.list_parts'),
    # ('^parts/distributors$', 'parts.views.list_distributors'),
    ('^parts/order/(?P<order_id>\d+)/$', 'parts.views.order_detail'),
    ('^parts/part/(?P<part_id>\d+)/$', 'parts.views.part_detail'),
)
