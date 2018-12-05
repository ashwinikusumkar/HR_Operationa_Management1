# Generated by Django 2.1.1 on 2018-12-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0011_applicant_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant_registration',
            name='idno',
        ),
        migrations.AlterField(
            model_name='applicant_registration',
            name='email',
            field=models.EmailField(max_length=60, primary_key=True, serialize=False),
        ),
    ]
