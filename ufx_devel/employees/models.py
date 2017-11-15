from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Employee(models.Model):
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    phone_regex = RegexValidator(regex = r'^42(0|1){1}\d{3}\d{3}\d{3}$', message='Phone number must be in format 421915123456')
    phone_number = models.CharField(validators = [phone_regex], max_length = 255)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    is_active= models.BooleanField(default = True)
    sim_card_number = models.CharField(max_length = 50, primary_key=True)


    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)
