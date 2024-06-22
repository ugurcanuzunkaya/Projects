from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
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

            message_body = f"A new job application has been submitted by {first_name} {last_name}. " 
            + f"Email: {email}, Available date: {available_date}, Occupation: {occupation}."

            email_message = EmailMessage(
                subject="New job application",
                body=message_body,
                to=[email],
            )
            email_message.send()

            messages.success(request, "Application form submitted successfully")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def homepage(request):
    return render(request, "homepage.html")