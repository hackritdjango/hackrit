from django.conf.urls import url, include 
from django.urls import path
from unmask.views import first,signup,home,complaint,notification,helpdesk,profile

urlpatterns= [
	path('unmask/hack/',first,name='first'),
	#path('unmask/login',login,name='login'),
	path('unmask/signup',signup,name='signup'),
	path('unmask/login/home',home,name='home'),
	path('unmask/login/complaint',complaint,name='complaint'),
	path('unmask/login/notification',notification,name='notification'),
	path('unmask/login/helpdesk',helpdesk,name='helpdesk'),
	path('unmask/login/profile',profile,name='profile'),
	#url('^unmask/login/notifications/', include(notifications.urls, namespace='notifications')),
]
from django.conf.urls import *
from . import views

from django.contrib import admin
admin.autodiscover()

#       url(r'^$', views.index, name='index'),
 #       url(r'^register_profile/$', views.register_profile, name='register_profile'),
  #      url(r'^(?P<username>\w+)/$', views.profile_page, name='user_profile'),
   #     )
