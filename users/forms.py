from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms 
from .models import CustomUser
from django.contrib.auth import login ,logout, authenticate


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


################################################Login###############################################
class LoginForm(forms.Form):
	email = forms.CharField(label= 'email')
	password = forms.CharField(label = 'password',widget = forms.PasswordInput)

	def clean(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		if email and password :
			user =authenticate(email = email , password = password )
			if not user:
				raise forms.ValidationError('the credintials you provided were incorreect please try again ')
			if not user.check_password(password):
				raise forms.ValidationError('password is incorreect please check your password and try again ')
			if not user.is_active:
				raise forms.ValidationError('please activate your account by clicking the email sent to you when you registred')
		return super(LoginForm,self).clean(*args,**kwargs)
############################################# password change form##################################