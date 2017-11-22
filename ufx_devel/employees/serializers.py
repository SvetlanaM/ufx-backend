from .models import Employee
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many = False, read_only = False)
    class Meta:
        model = Employee
        fields = [
            'employee',
        ]
