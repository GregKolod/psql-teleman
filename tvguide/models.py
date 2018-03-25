from django.contrib.postgres.fields import JSONField
from django.db import models


class TvGuide(models.Model):
    name = models.CharField(max_length=40)
    date_at = models.CharField(max_length=40, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Channel(models.Model):
    tvguide = models.ForeignKey(TvGuide, related_name='channels', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    quote_page = models.CharField(max_length=255, default='')
    daily_channel = JSONField(blank=True, null=True, default={})

    def __str__(self):
        return self.name
