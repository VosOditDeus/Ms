from django import forms
from models import Comment,Image, User
from django.forms import forms, ModelForm
from django.contrib.auth.forms import UserCreationForm

class PhotoForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'title', 'tags', 'albums']
class PhotoSearchTags(forms.Form):
    pass


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']