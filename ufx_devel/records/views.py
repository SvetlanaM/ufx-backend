from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .serializers import RecordSerializer
from rest_framework import generics,  permissions
from .models import Record

class RecordCreateAPIView(generics.CreateAPIView):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer
