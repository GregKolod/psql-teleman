from django.contrib.postgres.fields import JSONField
from django.db import models

from . import scrapers


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
    daily_channel = JSONField(blank=True, default='')

    class Meta:
        unique_together = ['name', 'tvguide']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.daily_channel:
            msg = 'Scraping: {}'.format(self.quote_page)
            print(msg)

            channel_list = scrapers.channel_scrapper(self.quote_page)
            self.daily_channel = {"channel_list": channel_list}
            super(Channel, self).save(*args, **kwargs)
