from django.shortcuts import render

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






