from django import forms
from models import Image
from django.forms import forms, ModelForm


class PhotoForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'title', 'tags', 'albums']
class ImageChangeForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'tags', 'albums']