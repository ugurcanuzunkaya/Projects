from django.urls import path
from . import views


urlpatterns = [
    path("", views.welcomepage, name="welcomepage"),
    path("application/", views.application, name="application"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
