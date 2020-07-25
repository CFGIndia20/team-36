from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# from .models import *
from .forms import *
from django.contrib import messages
from .whatsappAPI import send_message

# Create your views here.
@login_required(login_url='login')
def index(request):
	return HttpResponse("Dashboard Page")


def registerPage(request):
	if request.user.is_authenticated:
		return redirect("/dashboard/")
	else:
		form = CreateUserForm()
		if request.method == "POST":
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
			user = form.cleaned_data.get("username")
			messages.success(request,"Account was created for " + user)
			return redirect("/dashboard/")
		
		context = {'form':form}
		return render(request,"Dashboard/register.html",context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("/dashboard/")
	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request,username=username,password=password)
			
			if user is not None:
				login(request,user)
				return redirect("/dashboard/")
			else:
				messages.info(request,"Username or password is incorrect")

		return render(request,'Dashboard/login.html')
		
def logoutUser(request):
	logout(request)
	return redirect("/dashboard/login/")
	
