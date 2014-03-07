# app specific urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
                       (r'^home/', TemplateView.as_view(template_name="home.html")),
                   )
