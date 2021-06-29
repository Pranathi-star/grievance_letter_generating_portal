from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 10)
    email = models.EmailField()
    state = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    school = models.CharField(max_length = 200)

class Letter(models.Model):
    grievance =  models.CharField(max_length=200, null=True, default = 'water problems')
    name_smc = models.CharField(max_length=200, null=True, default = 'John')
    email_smc = models.EmailField(default = 'abc@xyz.com')
    school_smc = models.CharField(max_length=200, null=True, default = 'Vidya High School')
    state_smc = models.CharField(max_length=200, null=True, default = 'Telangana')
    city_smc = models.CharField(max_length=200, null=True, default = 'Hyderabad')
    date_posted = models.DateTimeField(default=timezone.now)

class GrievanceLetter(Letter):
    grievance_letter =  models.FileField()

