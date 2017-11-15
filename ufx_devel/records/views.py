from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .serializers import RecordSerializer
from rest_framework import generics,  permissions
from .models import Record
from rest_framework.parsers import MultiPartParser, FormParser

class RecordCreateAPIView(generics.CreateAPIView):
    serializer_class = RecordSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Record.objects.all()
    
