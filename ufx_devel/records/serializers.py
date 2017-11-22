from .models import Record, BlackList
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from employees.serializers import EmployeeSerializer

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    upload_to = serializers.FileField()
    employee = EmployeeSerializer(many = False, read_only = False)
    class Meta:
        model = Record
        fields = [
            'phone_number',
            'call_date',
            'upload_to',
            'call_type',
            'employee',
        ]


class BlackListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlackList
        fields = [
            'phone_number',
            'reason'
        ]
