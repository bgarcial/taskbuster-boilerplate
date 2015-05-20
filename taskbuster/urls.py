from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import home
#from .import views

#urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
#)
