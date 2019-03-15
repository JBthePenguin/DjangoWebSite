from django import forms
from websiteapp.models import get_placeholders
from websiteapp.contactapp.models import Message


class ContactForm(forms.ModelForm):
    """ class for the forms for add or update actu """

    class Meta:
        model = Message
        fields = ['contact_name', 'contact_email', 'subject', 'content']

    def __init__(self, *args):
        super(ContactForm, self).__init__(*args)
        placeholders = get_placeholders("contact")

        def set_label_widget(field_name, placeholder):
            """ no display label and update placeholder """
            self.fields[field_name].label = False
            self.fields[field_name].widget.attrs.update(
                {'placeholder': placeholder})
        # set inputs
        set_label_widget("contact_name", placeholders[0].text)
        set_label_widget("contact_email", placeholders[1].text)
        set_label_widget("subject", placeholders[2].text)
        set_label_widget("content", placeholders[3].text)
        self.fields["contact_name"].widget.attrs.update(
            {'autofocus': True})
