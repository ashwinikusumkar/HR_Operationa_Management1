# Generated by Django 2.1.1 on 2018-11-27 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0009_interviewer_registration_manager_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hr_registration',
            old_name='dob',
            new_name='doj',
        ),
        migrations.RenameField(
            model_name='interviewer_registration',
            old_name='dob',
            new_name='doj',
        ),
        migrations.RenameField(
            model_name='manager_registration',
            old_name='dob',
            new_name='doj',
        ),
    ]
