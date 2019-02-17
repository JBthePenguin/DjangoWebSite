from django import forms
from django.contrib import admin
from websiteapp.contactapp.models import Message


class MessageAdminForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ["read"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    form = MessageAdminForm
    search_fields = ('contact_name', 'contact_email', 'read')
    list_display = (
        'contact_name',
        'contact_email',
        'subject',
        'content',
        'date',
        'read',
    )
