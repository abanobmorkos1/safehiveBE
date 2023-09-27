from django.shortcuts import render
from .models import SafehiveDetails
from rest_framework import viewsets
from ..safehive.serializers import Hiveserializer

class safeHive(viewsets.ModelViewSet):
    queryset = SafehiveDetails.objects.all()
    serializer_class = Hiveserializer
