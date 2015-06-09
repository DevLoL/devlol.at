from django.contrib import admin
from diary.models import DiaryItem, EventLocation, ImageItem

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'start_time', 'author', 'location')
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.author = request.user
        obj.save()

# Register your models here.
admin.site.register(DiaryItem, DiaryAdmin)
admin.site.register(EventLocation)
admin.site.register(ImageItem)
