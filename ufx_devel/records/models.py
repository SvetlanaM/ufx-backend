from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from employees.models import Employee
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail
from decouple import config
import datetime
from django.db.models import Q

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
    is_recorded = models.NullBooleanField(default = True, null = True, blank = True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return "%s---%s" %(self.phone_number, self.call_date.strftime("%d.%m.%Y"))


def send_alert_email(sender, instance, **kwargs):

    now = datetime.datetime.now()
    now_1 = now - datetime.timedelta(hours=1)
    earlier = now - datetime.timedelta(hours=5)
    all_numbers = Record.objects.filter(Q(created_date__range=(earlier, now)) | Q(is_recorded = False))
    find_in = False
    count = 0
    for record in all_numbers:

        if record.employee.sim_card_number == instance.employee.sim_card_number:
            count +=1
        else:
            continue


    if instance.is_recorded == False and count == 1:
        subject = 'Nenahrávají se hovory'
        mesagge = 'Na čísle %s neprobíhá záznam hovorů zaměstnance %s %s.' %(instance.employee.phone_number, instance.employee.first_name, instance.employee.last_name)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, mesagge, from_email, [config('EMAIL_USER1')], fail_silently=False)
    all_numbers = []

post_save.connect(send_alert_email, sender=Record)

class BlackList(models.Model):
    phone_regex = RegexValidator(regex = r'^42(0|1){1}\d{3}\d{3}\d{3}$', message='Phone number must be in format 421915123456')
    phone_number = models.CharField(validators = [phone_regex], max_length = 255)
    is_blocked = models.BooleanField(default = True)
    reason = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name = "Blocked number"
        verbose_name_plural = "Blocked numbers"

    def __str__(self):
        return "%s" %(self.phone_number)
