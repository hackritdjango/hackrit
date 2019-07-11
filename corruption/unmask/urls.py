from django.conf.urls import url, include
from django.urls import path
from unmask.views import first,login,signup,home,complaint,notification,helpdesk,profile

urlpatterns= [
	path('unmask/hack/',first,name='first'),
	path('unmask/login',login,name='login'),
	path('unmask/signup',signup,name='signup'),
	path('unmask/login/home',home,name='home'),
	path('unmask/login/complaint',complaint,name='complaint'),
	path('unmask/login/notification',notification,name='notification'),
	path('unmask/login/helpdesk',helpdesk,name='helpdesk'),
	path('unmask/login/profile',profile,name='profile'),
	#url('^unmask/login/notifications/', include(notifications.urls, namespace='notifications')),
]
