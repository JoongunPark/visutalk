from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'visutalk.views.home', name='home'),
   url(r'^picture/', 'visutalk.views.picture'),
   url(r'^admin/', include(admin.site.urls)),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url('', include('django.contrib.auth.urls', namespace='auth')),
)