from .models import Image
from django import forms
from django.forms import ModelForm

class PhotoForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'title', 'tags']
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     '''
    #     do some stuff, it's just an example so whatever
    #     '''
class ImageChangeForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'tags']

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField()