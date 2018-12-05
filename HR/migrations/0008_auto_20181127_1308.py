# Generated by Django 2.1.1 on 2018-11-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0007_auto_20181127_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='HR_Registration',
            fields=[
                ('idno', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
                ('experience', models.IntegerField(null=True)),
                ('dob', models.DateField()),
                ('phone', models.IntegerField(null=True)),
                ('Address', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='HR',
        ),
    ]
