from django.shortcuts import render
from .forms import ApplicationForm, ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
import os


def welcomepage(request):
    return render(request, "welcomepage.html")


def application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            available_date = form.cleaned_data["available_date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                available_date=available_date,
                occupation=occupation,
            )

            message_body = f"A new job application has been submitted by {first_name} {last_name}. Email: {email}, Available date: {available_date}, Occupation: {occupation}."

            email_message = EmailMessage(
                subject="New job application",
                body=message_body,
                to=[email],
            )
            email_message.send()

            messages.success(request, "Application form submitted successfully")

    return render(request, "application.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            message_body = f"Name: {name}, Email: {email}, Message: {message}"

            email_message = EmailMessage(
                subject="Job Application Contact Us Form",
                body=message_body,
                to=[os.environ.get("EMAIL_HOST_USER")],
            )
            email_message.send()

            messages.success(request, "Contact form submitted successfully")

    return render(request, "contact.html")
