from django.urls import path ,re_path ,include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


#these are the urls that redirect to the function that actually runs the application

urlpatterns = [ 
    path('list_events/', views.list_events , name = 'list_events'),
	# path('tests', views.list_tests , name = 'list_test'),  
    path('delete_event/<int:id>/', views.delete_event , name = 'delete_event'),
    path('delete_test/<int:id>/', views.delete_test , name = 'delete_test'),
    path('emails_sent/<int:id>/', views.emails_sent , name = 'emails_sent'),
	path('complete/<int:id>/', views.complete , name = 'complete'),
	path('edit_event/<int:id>/', views.edit_event , name = 'edit_event'),
	path('update_event/<int:id>/', views.update_event , name = 'update_event'),
	path('add_video/<int:id>/', views.add_video , name = 'add_video'),
    # path('PasswordChange/', views.PasswordChange , name = 'PasswordChange'),    
]
