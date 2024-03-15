from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from decouple import config

import smtplib
from .models import ContactForm

def sendnote(nameemail,**kwargs):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        mymail = config('EMAIL_ADDR')
        password = config('EMAIL_PASS')

        connection.starttls()

        connection.login(user=mymail, password=password)

        if nameemail=="contact":
            connection.sendmail(from_addr=mymail, to_addrs=["agraradev2218@gmail.com", "akash.bhanushali@somaiya.edu", "karunesh.b@somaiya.edu"],
                                msg=f"Subject: New Project Request on GammaBytes\n\n Client Name: {kwargs['name']}\n\n Client Contact: {kwargs['contact']}\n\n Company: {kwargs['company']}\n\n Message: {kwargs['message']}\n\n")

def website_page(request):
    return render(request, 'gammabytes_site/index.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('contact-name')
        email = request.POST.get('contact-email')
        message = request.POST.get('contact-message')
        company = request.POST.get('contact-company')

        form = ContactForm(name=name, email=email, message=message, company=company)
        form.save()

        sendnote(nameemail="contact", name=name, contact=email, message=message, company=company)

        messages.success(request, "Form Submitted Successfully!")
        return render(request, 'gammabytes_site/index.html')
    else:
        return render(request, 'gammabytes_site/index.html')