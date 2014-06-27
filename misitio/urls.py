#CONDING: UTF-8
from django.conf.urls import patterns, include, url
from polls import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^polls/', include('polls.urls',namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    
)
