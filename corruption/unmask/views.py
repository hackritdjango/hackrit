from django.shortcuts import render,redirect 
from .models import Complaint,Compuser
from .forms import ComplaintForm,SignupForm
from django.db.models.signals import post_save
from django.contrib.auth import views as auth_views
#from django.notifications.signals import notify
#from myapp.models import MyModel
import operator
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.
def first(request):
	return render(request, 'unmask/hack.html',{})

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		print(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('hack')
	else:
	    form=SignupForm()
	    return render(request, 'unmask/signup.html',{"form": form})
def home(request):
	return render(request, 'unmask/home.html',{})
def complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        print(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            send_mail(
                'post.Crime',
                'post.description',
                'post.user.email',
            )
            return redirect('home')
    else:
        form=ComplaintForm()
        return render(request, 'unmask/complaint.html',{"form":form})
def notification(request):
	return render(request, 'unmask/notification.html',{})
def helpdesk(request):
	return render(request, 'unmask/helpdesk.html',{})
def profile(request):
	return render(request, 'unmask/profile.html')

