from django.db import models
from django.contrib.auth.models import User

class DiaryItem(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64, blank=True)
    link = models.URLField(blank=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    author = models.ForeignKey(User)
    location = models.ForeignKey('EventLocation')
    content = models.TextField()
    def __unicode__(self):
        return self.title + " - " + self.subtitle if self.subtitle else self.title

class EventLocation(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    def __unicode__(self):
        return self.name

class ImageItem(models.Model):
    data = models.ImageField(upload_to="images")
    diary_item = models.ForeignKey(DiaryItem)
