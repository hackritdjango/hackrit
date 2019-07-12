"""corruption URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('unmask.urls')),
    url(r'^unmask/login/$',auth_views.LoginView.as_view(),name='login')
]
#from django.conf.urls import patterns, url
#from howdidu import views
#from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from registration.backends.simple.views import RegistrationView
#from django.conf.urls.defaults import *


class MyRegistrationView():  #redirects to home page after registration
    def get_success_url(self,request, user):
        return '/register_profile'

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'howdidu_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('howdidu.urls')),
    #url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'), #redirects to home page after registration
   # (r'^accounts/', include('registration.backends.simple.urls')),
    #url(r'^(?P<username>\w+)/', include('howdidimport notifications.urls))

#urlpatterns = [
    #...
    #url('^uname/login/notifications/', include(notifications.urls, namespace='notifications')),
   #...
#]
#u.urls')), #do i need this?
#)

# media
#if settings.DEBUG:
 #   urlpatterns += patterns(
  #      'django.views.static',
   #     (r'^media/(?P<path>.*)',
    #    'serve',
     #   {'document_root': settings.MEDIA_ROOT}), )