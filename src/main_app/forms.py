from django import forms

from main_app.models import ContactMe


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ["title", "content"]
