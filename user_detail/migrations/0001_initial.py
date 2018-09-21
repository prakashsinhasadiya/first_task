# Generated by Django 2.0 on 2018-09-21 04:19

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('Name', models.CharField(max_length=30, verbose_name='Name')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Mobile', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^(\\+\\d{1,3})?,?\\s?\\d{8,13}')], verbose_name='Mobile')),
                ('Address', models.CharField(max_length=25, verbose_name='Address')),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='m', max_length=2, verbose_name='Gender')),
                ('Bloodgroup', models.CharField(choices=[('op', 'O+'), ('ap', 'A+'), ('bp', 'B+'), ('abp', 'AB+')], max_length=2, verbose_name='Blood Group')),
                ('Dob', models.DateField(verbose_name='Date of birth')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
