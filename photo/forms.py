from models import Comment
from django.forms import forms, ModelForm


class PhotoSubmit(forms.Form):
    pass


class PhotoSearchTags(forms.Form):
    pass


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
