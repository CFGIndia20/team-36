from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from django.contrib import messages
from .whatsappAPI import send_message

from django.views.generic import View
import pdfkit
from django.http import HttpResponse

from xhtml2pdf import pisa 
from django.template import Context

from django.template.loader import get_template

import os
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.http import FileResponse
import io
from reportlab.lib.units import inch

from twilio.rest import Client

def reportGenerator(request):
    # Returns some HTML as response
    return HttpResponse("<h1>Hello World</h1>")

def pdf(request ):

    count = "7"
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    name = "Palak Davda"
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # p.drawImage("https://ibb.co/PY2psYB", 0,0)
    # p.drawInlineImage( "/static/footer_image.png", inch*.25, inch*.25, PAGE_WIDTH-(.5*inch), (.316*inch))
    p.drawString(30, 755, "Dear " + name)
    p.drawString(30, 735, "We would like to express sincere thanks for helping us, and the needy childrens.")
    p.drawString(30, 720, "Your contribution is vital to our work")
    p.drawString(30,690,"Every child suffering from cancer, irrespective of economic status, deserves to get ")
    p.drawString(30,675,"the best chance of surviving the disease and leading a full, healthy, happy life. ")
    p.drawString(30,660,"St. Judes provides this chance through its well-established model of cost-free, holistic care")
    p.drawString(30,645,"during the period of the child's treatment. We were able to create an impact on the society, this")
    p.drawString(30,630, "kind of efforts is really much appreciated.")
    p.drawString(30,605, "It was only possible because of you, because of your $100 donation, we were able to help"+count+" childrens ")
    p.drawString(30,590,"suffering from fatal disease. We aim at extending help to all the people in need, and we would be able to")
    p.drawString(30, 575,"acheive this only by the support of our donors like.")


    
    p.drawString(30, 550, "Thank you again for your generous gift. It's only through supporters like you that ")
    
    p.drawString(30,535, "we will achieve our mission. We are looking forward to seeing you again!")

    p.drawString(30,505, "Best Wishes")
    p.drawString(30,490, "St Judes")

    # p.drawString(50, 850, "we would like to thank you." + name)

    # p.drawString(30, 750, "Hello Palak!.. Thanks for donating." + name)


    # canvas.drawInlineImagehttps://www.stjudechild.org/images/nl/feb2020/newsletter-jan2019.jpg, inch*.25, inch*.25, PAGE_WIDTH-(.5*inch), (.316*inch))
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


@login_required(login_url='login')
def index(request):
	send_message()
	return render(request,"Dashboard/index.html")

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
		return render(request,"Dashboard/register_2.html",context)

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

		return render(request,'Dashboard/login_2.html')
		
def logoutUser(request):
	logout(request)
	return redirect("/dashboard/login/")

@login_required(login_url='login')
def centers(request):
	return render(request,'Dashboard/Centers.html')

@login_required(login_url='login')
def beneficiaries(request):
	return render(request,'Dashboard/Children.html')

@login_required(login_url='login')
def child1(request):
	return render(request,'Dashboard/Child_1.html')

@login_required(login_url='login')
def child2(request):
	return render(request,'Dashboard/Child_2.html')


@login_required(login_url='login')
def donors(request):
	return render(request,'Dashboard/donors.html')

@login_required(login_url='login')
def donor1(request):
	return render(request,'Dashboard/Donor_1.html')

@login_required(login_url='login')
def donor2(request):
	return render(request,'Dashboard/Donor_2.html')

from twilio.twiml.messaging_response import MessagingResponse


def sendSms(request):
    account_sid = 'XXXX'
    auth_token = 'XXXX'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Welcome to CFG India 2020 !",
                     from_='+13392349976',
                     to='<your-number>'
                 )

    if message.sid:
        return HttpResponse('SMS sent')
    else:
        return HttpResponse('Error')