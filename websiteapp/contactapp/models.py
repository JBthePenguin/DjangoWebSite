from django.db import models


# Items
class ContactItem(models.Model):
    logo = models.CharField(db_index=True, max_length=255)
    text = models.CharField(db_index=True, max_length=255)
    position = models.IntegerField(db_index=True, default=0)


def get_all_contact_items():
    """ return all contact items """
    return ContactItem.objects.all().order_by('position')


# Message
class Message(models.Model):
    contact_name = models.CharField(db_index=True, max_length=255)
    contact_email = models.EmailField(db_index=True, max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    read = models.BooleanField(default=False)
