from rest_framework import serializers

from . import models


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'tvguide',
            'name',
            'daily_channel',
        )
        model = models.Channel
