from django.shortcuts import render_to_response
from diary.models import DiaryItem, ImageItem
import datetime
import status

context = {}
context['state'] = 'OPEN' in status.query_api()
context['events'] = DiaryItem.objects.filter(date__gt=datetime.date.today()).order_by('date', 'time');

def index(request):
    diary_items = DiaryItem.objects.filter(date__lte=datetime.date.today()).order_by('-date', '-time');
    for di in diary_items:
        image_items = ImageItem.objects.filter(diary_item=di)
        di.images = image_items
    context['items'] = diary_items
    return render_to_response("index.html", context)

def location(request):
    return render_to_response("location.html", context)

def projects(request):
    return render_to_response("projects.html", context)

def members(request):
    return render_to_response("members.html", context)

def join(request):
    return render_to_response("join.html", context)

def monitoring(request):
    return render_to_response("monitoring.html", context)

def equipment(request):
    return render_to_response("equipment.html", context)
