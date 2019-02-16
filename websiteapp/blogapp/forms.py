from django import forms
from websiteapp.blogapp.models import Comment


class CommentForm(forms.ModelForm):
    """ class for the forms for add or update actu """
    class Meta:
        model = Comment
        fields = ['author_name', 'author_email', 'text']

    def __init__(self, *args, **kwargs):
        self.language = kwargs.pop('language')
        super(CommentForm, self).__init__(*args, **kwargs)
        if self.language == "fr":
            placeholder_name = "Nom"
            placeholder_text = "".join(["é".upper(), "crire un commentaire"])
        else:
            placeholder_name = "Name"
            placeholder_text = "Enter a comment"
        self.fields['author_name'].label = False
        self.fields['author_email'].label = False
        self.fields['text'].label = False
        self.fields['author_name'].widget.attrs.update(
            {'placeholder': placeholder_name})
        self.fields['author_email'].widget.attrs.update(
            {'placeholder': "Email"})
        self.fields['text'].widget.attrs.update(
            {'placeholder': placeholder_text})
        self.fields['author_email'].error_messages = {
            'invalid': 'invalid email'}
