from django.shortcuts import get_object_or_404

from rest_framework import generics

from . import models
from . import serializers


class ListCreateTvGuide(generics.ListCreateAPIView):
    queryset = models.TvGuide.objects.all()
    serializer_class = serializers.TvGuideSerializer
