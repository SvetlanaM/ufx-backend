from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .serializers import RecordSerializer, BlackListSerializer
from rest_framework import generics,  permissions
from .models import Record, BlackList
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.response import Response

class RecordCreateAPIView(generics.CreateAPIView):
    serializer_class = RecordSerializer
    parser_classes = (MultiPartParser, FileUploadParser,)
    queryset = Record.objects.all()

    def perform_create(self, serializer):
        data = self.request.data

        if self.request.data.get('is_recorded') == '0' or self.request.data.get('is_recorded') == 'False':
            is_recorded = bool(0)
        else:
            is_recorded = bool(1)

        serializer.save(
            phone_number = data['phone_number'],
            upload_to = self.request.data.get('upload_to'),
            call_date = data['call_date'],
            is_recorded = is_recorded
        )
        return Response({'received data': self.request.data})

class BlackListAPIView(generics.ListAPIView):
    queryset = BlackList.objects.filter(is_blocked = True)
    serializer_class = BlackListSerializer
