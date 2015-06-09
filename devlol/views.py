from django.shortcuts import render_to_response, redirect
from diary.models import DiaryItem, ImageItem
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from markdown import markdown
from urllib import urlopen
from icalendar import Calendar, Event, vText
import datetime
import status
import pytz

#### Disclaimer ####
# honestly - this file is a mess
# my idea is to write as messy as possible to encourage some other devs to help improving this ;)
# this shouldn't be a one-man-show

def get_events():
    # limit to 5
    events = DiaryItem.objects.filter(start_date__gt=datetime.date.today()).order_by('start_date', 'start_time');
    for e in events:
        e.datestring = e.start_date.strftime("%d.%m.%Y")
        e.timestring = e.start_time.strftime("%H:%M")
    return events

def index(request):
    context = {}
    context['state'] = status.isOpen()
    context['events'] = get_events()
    context.update(csrf(request))
    # limit to 10 - 15
    diary_items = DiaryItem.objects.filter(start_date__lte=datetime.date.today()).order_by('-start_date', '-start_time');
    for di in diary_items:
        di.html = markdown(di.content)
        di.datestring = di.start_date.strftime("%d.%m.%Y")
        di.timestring = di.start_time.strftime("%H:%M Uhr")
        image_items = ImageItem.objects.filter(diary_item=di)
        di.images = image_items
    context['items'] = diary_items
    return render_to_response("index.html", context)

def location(request):
    context = {}
    context['state'] = status.isOpen()
    context['events'] = get_events()
    context.update(csrf(request))
    return render_to_response("location.html", context)

def projects(request):
    context.update(csrf(request))
    content = urlopen("https://devlol.org/wiki/projects?action=content")
    context['content'] = content.read()
    return render_to_response("projects.html", context)

def members(request):
    context.update(csrf(request))
    return render_to_response("members.html", context)

def join(request):
    context.update(csrf(request))
    return render_to_response("join.html", context)

def monitoring(request):
    context.update(csrf(request))
    return render_to_response("monitoring.html", context)

def equipment(request):
    context.update(csrf(request))
    return render_to_response("equipment.html", context)

def mail(request):
    if request.POST:
        mail = request.POST['mail_entry']
        try:
            send_mail('Subscription request', '', mail, ['devlol-join@lists.servus.at'], fail_silently=False)
        except:
            print "an error occured"
    return redirect('/')

def events(request):
    events = DiaryItem.objects.filter(start_date__gt=datetime.date.today()).order_by('start_date', 'start_time').values('title', 'start_date', 'start_time', 'subtitle');
    return JsonResponse({'events': list(events)})

def ical(request):
    cal = Calendar()
    cal.add('prodid', '-// /dev/lol - Event Calendar - devlol.at //')
    cal.add('version', '2.0')
    begin = datetime.date.today() - datetime.timedelta(days=32)
    events = DiaryItem.objects.filter(start_date__gt=begin).order_by('start_date', 'start_time');
    for e in events:
        event = Event()
        if e.subtitle:
            event.add('summary', e.title + " - " + e.subtitle)
        else:
            event.add('summary', e.title)
        event.add('dtstart', datetime.datetime.combine(e.start_date, e.start_time))
        event.add('dtend', datetime.datetime.combine(e.end_date, e.end_time))
        event['location'] = vText(e.location)
        event['description'] = vText(e.content)
        cal.add_component(event)
    response = HttpResponse(cal.to_ical(), 'text/calendar')
    response['Content-Disposition'] = 'attachment; filename=events.ics'
    return response
