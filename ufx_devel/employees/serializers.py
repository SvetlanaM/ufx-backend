from .models import Employee
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'sim_card_number',
        ]