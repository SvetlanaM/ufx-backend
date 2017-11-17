from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from datetime import datetime
from employees.models import Employee

CALL_TYPES = (
    ('1','Incoming'),
    ('2','Outcoming'),
)


class Record(models.Model):
    phone_regex = RegexValidator(regex = r'^42(0|1){1}\d{3}\d{3}\d{3}$', message='Phone number must be in format 421915123456')
    phone_number = models.CharField(validators = [phone_regex], max_length = 255)
    call_date = models.DateTimeField(auto_now_add = False)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    is_archived = models.BooleanField(default = False)
    upload_to = models.FileField(upload_to='', blank = True, null = True)
    call_type = models.CharField(max_length = 1, choices = CALL_TYPES, blank = True, null = True)
    employee = models.ForeignKey('employees.Employee', models.SET_NULL, blank = True, null = True)


    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return "%s---%s" %(self.phone_number, self.call_date.strftime("%d.%m.%Y"))

class BlackList(models.Model):
    phone_regex = RegexValidator(regex = r'^42(0|1){1}\d{3}\d{3}\d{3}$', message='Phone number must be in format 421915123456')
    phone_number = models.CharField(validators = [phone_regex], max_length = 255)
    is_blocked = models.BooleanField(default = True)

    class Meta:
        verbose_name = "Blocked number"
        verbose_name_plural = "Blocked numbers"

    def __str__(self):
        return "%s" %(self.phone_number)
