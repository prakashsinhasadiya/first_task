from django.db import models
from django.core.validators import RegexValidator
from model_utils.models import TimeStampedModel

# Create your models here.


class UserProfile(TimeStampedModel):

    Name = models.CharField(verbose_name="Name",
                            max_length=30)
    Email = models.EmailField(verbose_name="Email"
                              )

    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Mobile = models.CharField(verbose_name="Mobile", validators=[
                              phone_regex], max_length=17)

    Address = models.CharField(verbose_name="Address",max_length=25)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    BLOOD_GROUP_CHOICE = (
        ('op', 'O+'),
        ('ap', 'A+'),
        ('bp', 'B+'),
        ('abp', 'AB+'),
    )

    Gender = models.CharField(
        verbose_name="Gender", choices=GENDER_CHOICES, default='M',max_length=2)

    Bloodgroup = models.CharField(verbose_name="Blood Group", default="op",choices=BLOOD_GROUP_CHOICE,max_length=2)

    Dob = models.DateField(verbose_name="Date of birth")

    def __str__(self):
        return self.name
