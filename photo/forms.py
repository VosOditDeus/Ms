from models import Comment,Image
from django.forms import forms, ModelForm


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
