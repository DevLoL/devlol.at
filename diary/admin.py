from django.contrib import admin
from diary.models import DiaryItem, EventLocation, ImageItem

# Register your models here.
admin.site.register(DiaryItem)
admin.site.register(EventLocation)
admin.site.register(ImageItem)
