from django import forms
from django.db.models import fields
from .models import Contact, Publisher

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','mobile','message')

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name','address','city','state','country','website')