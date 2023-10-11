from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact", views.ContactMeView.as_view(), name="contact"),
]
