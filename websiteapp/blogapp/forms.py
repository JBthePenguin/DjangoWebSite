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
            placeholder_name = "Votre nom"
            placeholder_email = "Votre email"
            placeholder_text = "Votre commentaire"
        else:
            placeholder_name = "Your name"
            placeholder_email = "Your email"
            placeholder_text = "Your comment"

        def set_label_widget(field_name, placeholder):
            """ no display label and update placeholder """
            self.fields[field_name].label = False
            self.fields[field_name].widget.attrs.update(
                {'placeholder': placeholder})
        # set inputs
        set_label_widget("author_name", placeholder_name)
        set_label_widget("author_email", placeholder_email)
        set_label_widget("text", placeholder_text)
        self.fields['author_email'].error_messages = {
            'invalid': 'invalid email'}
