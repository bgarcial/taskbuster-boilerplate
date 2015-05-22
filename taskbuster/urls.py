# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files


#from .import views

#urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.HomeView.as_view(), name='home'),
    #url(r'^$', home, name='home'),

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    #Es una expresion regular que toma el url deseada y pasa en ella como argumento
    #el nombre del archivo sear robots.txt o humans.txt
]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)



