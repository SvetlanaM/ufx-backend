from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .serializers import RecordSerializer
from rest_framework import generics,  permissions
from .models import Record
from rest_framework.parsers import MultiPartParser, FormParser

class RecordCreateAPIView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def post(self, request, format=None):
        my_file = request.FILES['upload_to']
        filename = '/tmp/myfile'
        with open(filename, 'wb+') as temp_file:
            for chunk in my_file.chunks():
                temp_file.write(chunk)

        my_saved_file = open(filename) #there you go
