from django.db import models

# Create your models here.


# Company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=250)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile Phones', 'Mobile Phones')))
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


# Employee Model

class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=200, choices=(('Manager', 'manager'), ('Software Developer', 'sd'), ('Project Leader', 'pl')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


