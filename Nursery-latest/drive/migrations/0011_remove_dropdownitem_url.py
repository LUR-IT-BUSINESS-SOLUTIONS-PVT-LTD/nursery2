# Generated by Django 4.2.5 on 2024-01-11 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0010_remove_navbar_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dropdownitem',
            name='url',
        ),
    ]
