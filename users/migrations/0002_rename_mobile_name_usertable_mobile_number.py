# Generated by Django 4.0.4 on 2022-04-13 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertable',
            old_name='mobile_name',
            new_name='mobile_number',
        ),
    ]
