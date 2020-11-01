from django import forms
from . models import  events,tests



class event_creation_form(forms.ModelForm):
	class Meta:
		model = events
		fields = {'date','time','duration','country','topic','client','website','emails','embeded','auto_test_creation'}


class test_creation_form(forms.ModelForm):
	class Meta:
		model = tests
		fields = {'date','time','country','topic','client','emails'}


class edit_event_form(forms.ModelForm):
	class Meta:
		model = events
		fields=  {'date','time','country','topic','website','emails','embeded','client',}

class add_video(forms.ModelForm):
	class Meta:
		model = events
		fields=  {'video',}