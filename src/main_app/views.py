from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from main_app.forms import ContactMeForm


class IndexView(TemplateView):
    template_name = "index.html"


class ContactMeView(CreateView):
    template_name = "contact-me.html"
    form_class = ContactMeForm
    success_url = reverse_lazy("index")
