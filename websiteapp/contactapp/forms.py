from django import forms
from websiteapp.contactapp.models import Message


class ContactForm(forms.ModelForm):
    """ class for the forms for add or update actu """

    class Meta:
        model = Message
        fields = ['contact_name', 'contact_email', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        self.language = kwargs.pop('language')
        super(ContactForm, self).__init__(*args, **kwargs)
        if self.language == "fr":
            placeholder_name = "Votre nom"
            placeholder_email = "Votre email"
            placeholder_subject = "Objet"
            placeholder_content = "Votre message"
        else:
            placeholder_name = "Your name"
            placeholder_email = "Your email"
            placeholder_subject = "Subject"
            placeholder_content = "Your message"

        def set_label_widget(field_name, placeholder):
            """ no display label and update placeholder """
            self.fields[field_name].label = False
            self.fields[field_name].widget.attrs.update(
                {'placeholder': placeholder})
        # set inputs
        set_label_widget("contact_name", placeholder_name)
        set_label_widget("contact_email", placeholder_email)
        set_label_widget("subject", placeholder_subject)
        set_label_widget("content", placeholder_content)
        self.fields["contact_name"].widget.attrs.update(
            {'autofocus': True})
        self.fields['contact_email'].error_messages = {
            'invalid': 'invalid email'}
