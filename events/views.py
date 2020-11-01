from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import events,tests
from .filters import FilterEvents,FilterTests
from  users.models import CustomUser
from .forms import event_creation_form , test_creation_form,edit_event_form,add_video
from datetime import datetime,date
import datetime as timedel
from django.core.mail import send_mail

################################################### list Events###########################################
@login_required
def list_events(request):
	user = request.user
	print('loaded the form')
	form1 = event_creation_form(request.POST or None)
	form2 = test_creation_form(request.POST or None)
	# form3 = add_video(request.POST or None)	


############################################ add eventsform ##############################################
	if request.method == 'POST' and 'add_event' in request.POST:
		print('adding event if form is valid')
		if form1.is_valid():
			print('form is valid , adding the event')
			event = form1.save(commit = False)
			user = request.user
			event.user_id =user.id
			print(form1)
			event.save()
			if not event.auto_test_creation:
				message = '%(owner)s has added a new event on the %(date)s at %(time)s' % {'owner':user.name,'date':event.date,'time':event.time,}
				notification(event.topic,message)
			if event.auto_test_creation:
				test = form2.save(commit = False)
				test.user_id = user.id
				test.topic = event.topic
				test.date = event.date
				event_time = event.time
				event_time=event_time.strftime('%H:%M %p')
				number_of_min = '00:30:00'
				format = '%H:%M %p'
				prior = datetime.strptime(event_time, format)-timedel.timedelta(minutes = 30)
				test.time =  prior
				test.event_id = event.id
				test.country = event.country
				test.client = event.client
				test.emails = event.emails
				test.save()
				message = '%(owner)s has added a new event on the %(date)s at %(time)s and the rehearsal will be 30 min before country is %(country)s' % {'owner':user.name,'date':event.date,'time':event.time,'country':event.country,}
				notification(event.topic,message)

			else:
				pass
			return redirect('/list_events')
		else:
			print('form is not valid')
			event_creation_form()
############################################ add TEST form ##############################################
	elif request.method == 'POST' and 'add_test' in request.POST:
		print('adding test if form is valid')
		if form2.is_valid():
			print('form is valid , adding the test')
			test = form2.save(commit = False)
			user = request.user
			test.user_id = user.id
			event = events.objects.get(topic = test.topic)
			if not event.complete:
				event_id = event.id
				test.event_id = event_id
				test.save()
				message = '%(owner)s has added a new test on the %(date)s at %(time)s  country is %(country)s' % {'owner':user.name,'date':test.date,'time':test.time,'country':test.country,}
				notification(event.topic,message)
			return redirect('/list_events')
##############################################add video####################################################
	elif request.method == 'POST' and 'add_video' in request.POST:
		print('adding video if form is valid')
		# form3 = add_video(request.POST or None)	
		event_url = request.POST.get('video')
		event_id = request.POST.get('id')
		add_video(event_id,event_url)

############################################## today's events#############################################
	todays_events = events.objects.filter(date=date.today())
############################################## today's events#############################################
	todays_tests = tests.objects.filter(date=date.today())
##################################################show users################################################
	event = events.objects.all().order_by('date','time')
	test = tests.objects.all().order_by('date','time')
	tests_filter = FilterTests(request.GET , queryset  = test)
	events_filter = FilterEvents(request.GET , queryset  = event)
	return render (request,'events/events.html',{
		'filter1':events_filter,'form1':form1,'form2':form2,'filter2':tests_filter,
		'todays_events':todays_events,'todays_tests':todays_tests})
#################################################### delete event ###########################################
@login_required
def delete_event(request,id):
	user = request.user
	event = events.objects.get(id=id)
	if  event.user_id == user.id or user.level == 1 :
		event.delete()
		topic_tests = tests.objects.filter(topic = event.topic)
		topic_tests.delete()
		message = '%(owner)s has deleted this event %(topic)s' % {'owner':user.name,'topic':event.topic,}
		notification(event.topic,message)
		return redirect('list_events')
	return render(request,'events/delete_event.html',{'event':event})
#############################################complete###################################################
def complete (request,id):
	user = request.user
	if user.level == 1:
		event = events.objects.get(id = id)
		event.complete = True
		event.save()
		test = tests.objects.filter(event_id = id)
		topic_tests = tests.objects.filter(topic = event.topic)
		topic_tests.delete()
		test.delete()		
		message = 'this event %(topic)s has been marked as complete by %(user)s '%{'topic':event.topic,'user':user.name,}
		notification_for_users(event.topic,message,event.user.email)
		return redirect('list_events')
	else:
		return redirect('list_events')
#################################################### delete test ###########################################
@login_required
def delete_test(request,id):
	print('delete')
	user = request.user
	test = tests.objects.get(id=id)
	if test.user_id == user.id or user.level == 1  :
		test.delete()
		message = '%(owner)s has deleted this test %(topic)s' % {'owner':user.name,'topic':test.topic,}
		notification(test.topic,message)		
		return redirect('list_events')
	return render(request,'events/delete_test.html',{'test':test})	

##########################################edit event#######################################################
def edit_event(request,id):
	user = request.user
	event = events.objects.get(id = id)
	print (event)
	intial_data = {
	'date':event.date,'topic':event.topic,
	'time':event.time,'website':event.website,
	'emails':event.emails,'client':event.client,
	'country':event.country,'embeded':event.embeded,
	'duration':event.duration,
	}
	intial = intial_data
	form = edit_event_form( intial_data,request.POST or None)
	return render(request,'events/editEvent.html',{'form':form,'event':event})


def update_event(request,id):
	user = request.user
	if user.level == 1 or user.id == event.user_id:
		event = events.objects.get(id = id)
		event.date = request.POST.get('date')
		# event.date = datetime.strptime(string, '%Y-%m-%d').date()
		event.country = request.POST.get('country')
		event.topic = request.POST.get('topic')
		event.website = request.POST.get('website')
		event.emails = request.POST.get('emails')
		event.embeded = request.POST.get('embeded')
		event.client = request.POST.get('client')
		# event.duration = request.POST.get('duration')
		event.save()
		message = '%(owner)s has updated this event %(topic)s' % {'owner':user.name,'topic':event.topic,}
		notification(event.topic,message)
		redirect('list_events')
	return redirect('list_events')	
##################################################emails sent################################################
@login_required
def emails_sent(request,id):
	user = request.user
	if user.id == 1:
		event = events.objects.get(id=id)
		if event.notification:
			event.notification = False
			event.save()
			return redirect('list_events')
		else:
			event.notification = True
			event.save()
			message = 'emails  for the event %(topic)s has been sent to the presenters'%{'topic':event.topic}
			notification_for_users(event.topic,message,event.user.email)
			return redirect('list_events')
	else:
		return redirect('list_events')
#################################################add video link###############################################
def add_video(id,url):	
	event = events.objects.get(id = id)
	event.video = url
	event.save()
	message = 'the video link for the event %(topic)s is now ready'%{'topic':event.topic}
	notification_for_users(event.topic,message,event.user.email)
	redirect('list_events')
#############################################email notifications########################################
def notification(topic,message):
	send_mail(
	    topic,
	    message,
	    'meetings@reseller.orevan.org',
	    ['kikokhaled.u@gmail.com'],
	    fail_silently=False,
	)
#############################################email notifications for users ###############################
def notification_for_users(topic,message,mail):
	send_mail(
	    topic,
	    message,
	    'meetings@reseller.orevan.org',
	    [mail],
	    fail_silently=False,
	)
