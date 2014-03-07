# project wide urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib import admin
admin.autodiscover()
import settings

# import your urls from each app here, as needed
import Param_types.urls

urlpatterns = patterns('',
                       
                       # urls specific to this app
                       url(r'^Param_types/', include(Param_types.urls)),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       
                       # catch all, redirect to Param_types home view
                       url(r'^.*/$', TemplateView.as_view(template_name="home.html")),
                       
                   )
