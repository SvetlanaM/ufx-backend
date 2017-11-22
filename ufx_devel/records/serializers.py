from .models import Record, BlackList
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from employees.serializers import EmployeeSerializer
from employees.models import Employee

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    upload_to = serializers.FileField()
    #employee = EmployeeSerializer(many = False, read_only = False)
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many = False, read_only = False)


    class Meta:
        model = Record
        fields = [
            'id',
            'phone_number',
            'call_date',
            'upload_to',
            'call_type',
            'employee',
            'is_recorded',
        ]
        extra_kwargs = {'upload_to': {'read_only': False, 'required': False}}



class BlackListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlackList
        fields = [
            'phone_number',
            'reason'
        ]
