# Generated by Django 2.2.4 on 2019-08-07 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persona',
            new_name='Visitor',
        ),
    ]
