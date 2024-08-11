from django import forms
from django.forms import ModelForm
from .models import Contact, Project, Mockup, Site_data

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class MockupForm(ModelForm):
    class Meta:
        model = Mockup
        fields = "__all__"