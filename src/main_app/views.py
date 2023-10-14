import logging

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from main_app.forms import ContactMeForm

logger = logging.getLogger("app")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        print("This is debug print")
        logger.info("This is a debug log message")
        return super().get_context_data(**kwargs)


class ContactMeView(CreateView):
    template_name = "contact-me.html"
    form_class = ContactMeForm
    success_url = reverse_lazy("index")
