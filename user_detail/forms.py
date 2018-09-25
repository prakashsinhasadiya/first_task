# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

class UserDetailsForm(forms.Form):

    name = forms.CharField(label="Name", max_length=30, required=True, widget=forms.TextInput(attrs={'class': "form-control",'id':"name",'placeholder': 'Name'}))
    address = forms.CharField(label="Address" ,max_length=30, required=True, widget=forms.TextInput(attrs={'class': "form-control address",'id':"address",'placeholder': 'address'}))
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = forms.CharField(label="Mobile" ,validators=[phone_regex],max_length=17, required=True,
                             widget=forms.TextInput(attrs={'class': "form-control",'id':"mobile",'placeholder': 'mobile number'}))
    email = forms.EmailField(label="Email",
        required=True, widget=forms.EmailInput(attrs={'class': "form-control",'id':"email",'placeholder': 'Email'}))
    dob = forms.DateTimeField(label="Date of Birth", initial=datetime.now(),widget=forms.DateInput(attrs={'type':'date','id':"dob",'class': "form-control",'placeholder': 'date of birth'}))
    
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = forms.ChoiceField(label="Gender" ,widget=forms.RadioSelect(attrs={'class': "form-control",'id':"gender",'placeholder': 'gender'}), required=True,choices=gender_choices)
    
    blood_group_choice = (
        ('op', 'O+'),
        ('ap', 'A+'),
        ('bp', 'B+'),
        ('abp', 'AB+'),
    )

    blood_group= forms.ChoiceField(label="Blood Group", choices=blood_group_choice,widget=forms.Select(attrs={'class': "form-control",'id':"blood_group",'placeholder': 'blood groups'}  ),required=True)

