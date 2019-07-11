from django.shortcuts import render

# Create your views here.
def first(request):
	return render(request, 'unmask/hack.html',{})

def login(request):
	return render(request, 'unmask/login.html',{})
def signup(request):
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

