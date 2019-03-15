from django import forms
from websiteapp.models import get_placeholders
from websiteapp.blogapp.models import Comment


class CommentForm(forms.ModelForm):
    """ form to add a comment """
    class Meta:
        model = Comment
        fields = ['author_name', 'author_email', 'text']

    def __init__(self, *args):
        super(CommentForm, self).__init__(*args)
        placeholders = get_placeholders("comment")

        def set_label_widget(field_name, placeholder):
            """ no display label and update placeholder """
            self.fields[field_name].label = False
            self.fields[field_name].widget.attrs.update(
                {'placeholder': placeholder})
        # set inputs
        set_label_widget("author_name", placeholders[0].text)
        set_label_widget("author_email", placeholders[1].text)
        set_label_widget("text", placeholders[2].text)
