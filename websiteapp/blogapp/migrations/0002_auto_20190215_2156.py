# Generated by Django 2.1.6 on 2019-02-15 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='autor_name',
            new_name='author_name',
        ),
    ]