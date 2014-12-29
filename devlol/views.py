from django.shortcuts import render_to_response
from diary.models import DiaryItem, ImageItem
import datetime

def index(request):
    diary_items = DiaryItem.objects.filter(date__lte=datetime.date.today()).order_by('-date', '-time');
    for di in diary_items:
        image_items = ImageItem.objects.filter(diary_item=di)
        di.images = image_items
    events = DiaryItem.objects.filter(date__gt=datetime.date.today()).order_by('date', 'time');
    return render_to_response("index.html", {"items": diary_items, "events": events})

def location(request):
    return render_to_response("location.html")

def projects(request):
    return render_to_response("projects.html")

def members(request):
    return render_to_response("members.html")

def join(request):
    return render_to_response("join.html")
