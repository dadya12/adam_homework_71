from django import forms
from webapp.models import Publication, Comment


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['picture', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


