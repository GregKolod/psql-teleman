from django.shortcuts import get_object_or_404

from rest_framework import generics

from . import models
from . import serializers


class ListCreateTvGuide(generics.ListCreateAPIView):
    queryset = models.TvGuide.objects.all()
    serializer_class = serializers.TvGuideSerializer


class RetrieveUpdateDestroyTvGuide(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TvGuide.objects.all()
    serializer_class = serializers.TvGuideSerializer


class ListCreateChannel(generics.ListCreateAPIView):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer

    def get_queryset(self):
        return self.queryset.filter(tvguide_id=self.kwargs.get('tvguide_pk'))

    def perform_create(self, serializer):
        tvguide = get_object_or_404(models.TvGuide, pk=self.kwargs.get('tvguide_pk'))
        serializer.save(tvguide=tvguide)


class RetrieveUpdateDestroyChannel(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            tvguide_id=self.kwargs.get('tvguide_pk'),
            pk=self.kwargs.get('pk')
        )
