from django.shortcuts import render , redirect
from . forms import  LoginForm
from django.contrib.auth import get_user_model,views as auth_views,update_session_auth_hash
from django.contrib.auth import login ,logout, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.conf import settings 


User = get_user_model()


#####################################################login###############################################
def loginpage(request):
	user= request.user
	if not user.is_authenticated:
		form = LoginForm(request.POST or None)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(username = email , password = password)
			if not user.is_active:
				raise ValidationError('account is disabled contact the administrator')
			login (request,user)
			return redirect('/choosepage/')
		else:
			LoginForm()
		context = {
			'form':form,
		}
		return render (request,'users/login.html',context)
	else:
		return	redirect('/choosepage')

#####################################################choose page#########################################
@login_required
def choosepage(request):
	return render (request,'users/choosepage.html')
#################################################### logout##############################################
def logoutpage(request):
	logout(request)
	return redirect('/')


################################################## list Tests############################################
@login_required
def list_tests(request):
	return render (request,'users/tests.html')
##################################################Password change form###################################


@login_required
def PasswordChange(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			return redirect ('/choosepage/')
		else:
			messages.error(request,'please correct the errors below')
			#form = PasswordChangeForm(request.user)
	else:
		form = PasswordChangeForm(request.user)
	context = {

	'form':form,

	}
	return render(request,'users/ChangePasswordPage.html',context)


