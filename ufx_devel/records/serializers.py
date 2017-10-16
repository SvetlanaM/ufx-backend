from .models import Record
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='create-order', lookup_field = 'pk')
    class Meta:
        model = Record
        fields = [
            #'id',
            #'url',
            'phone_number',
            'call_date',
            'upload_to',
            'call_type',
        ]
