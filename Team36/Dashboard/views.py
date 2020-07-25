from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# from .models import *
from .forms import *
from django.contrib import messages
from .whatsappAPI import send_message

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
from reportlab.lib.units import inch

def reportGenerator(request):
    # Returns some HTML as response
    return HttpResponse("<h1>Hello World</h1>")

def pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    name = "palak davda"
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # p.drawImage("https://ibb.co/PY2psYB", 0,0)
    # p.drawInlineImage( "/static/footer_image.png", inch*.25, inch*.25, PAGE_WIDTH-(.5*inch), (.316*inch))
    p.drawString(30, 750, "Hello " + name)
    p.drawString(30, 735, "Thanks for your contribution")
    p.drawString(30, 700, "Your contribution is vital to our work")
    
    
    p.drawString(30, 685, "Thankyou again for your generous gift. It's only through supporters like you that ")
    
    p.drawString(30,670, "we will achieve our mission")
    p.drawString(30,650, "Because of your $100 donation, we were able to help 7 childrens suffering from fatal disease")

    p.drawString(30,600, "Best Wishes")
    p.drawString(30,580, "St Juges")

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
	return HttpResponse("<a href='/dashboard/pdf'>Hello World</a>")

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
	




# sending message

# from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
# from twilio.rest import Client

# def load_twilio_config(request):
#     account_sid = 'AC7f3ec6f3c60afb80126b6b8df39bfc44'
#     auth_token = '107acd298115ef1aaed81e1dae4efb01'
#     client = Client(account_sid, auth_token)

#     message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+14155238886',
#                      to='+918985607459' 
#                  )

#     print(message.sid)