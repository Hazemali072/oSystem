from django.urls import path ,re_path ,include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


#these are the urls that redirect to the function that actually runs the application

urlpatterns = [
	path('',views.loginpage,name = 'login'),#home
    path('choosepage/',views.choosepage, name= 'choosepage'),
    path('logoutpage/', views.logoutpage , name = 'logoutpage'),    
    path('list_tests/', views.list_tests , name = 'list_tests'),
    path('PasswordChange/', views.PasswordChange , name = 'PasswordChange'),    
]
