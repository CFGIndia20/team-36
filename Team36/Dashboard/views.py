from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# from .models import *
from .forms import *
from django.contrib import messages

from django.views.generic import View
import pdfkit
from django.http import HttpResponse
# Create your views here.
from xhtml2pdf import pisa 
from django.template import Context

from django.template.loader import get_template

import os
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.http import FileResponse
import io

def reportGenerator(request):
    # Returns some HTML as response
    return HttpResponse("<h1>Hello World</h1>")

def pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    name = "palak"
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world." + name)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')






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
	
