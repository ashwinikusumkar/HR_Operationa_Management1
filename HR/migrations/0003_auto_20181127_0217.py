# Generated by Django 2.1.1 on 2018-11-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_hr_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr_registration',
            name='phone',
            field=models.IntegerField(max_length=12),
        ),
    ]