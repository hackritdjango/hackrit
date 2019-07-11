from django.shortcuts import render
from .models import Complaint,Compuser
from .forms import ComplaintForm,SignupForm
from django.db.models.signals import post_save
#from notifications.signals import notify
#from myapp.models import MyModel

# Create your views here.
def first(request):
	return render(request, 'unmask/hack.html',{})

def login(request):
	return render(request, 'unmask/login.html',{})
def signup(request):
#	if request.method == "POST":
	#	form = SignupForm(request.POST)
	#	print(request.POST)
	#	if form.is_valid():
		#	post = form.save(commit=False)
		#	post.author = request.user
		#	post.save()
		#	return redirect('first')
	#else:
	form=SignupForm()
	return render(request, 'unmask/signup.html',{})
def home(request):
	return render(request, 'unmask/home.html',{})
def complaint(request):
	return render(request, 'unmask/complaint.html',{})
def notification(request):
	return render(request, 'unmask/notification.html',{})
def helpdesk(request):
	return render(request, 'unmask/helpdesk.html',{})
def profile(request):
	return render(request, 'unmask/profile.html')

#def my_handler(sender, instance, created, **kwargs):
    #notify.send(instance, verb='was saved')

#post_save.connect(my_handler, sender=MyModel)


