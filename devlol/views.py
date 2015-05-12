from django.shortcuts import render_to_response, redirect
from diary.models import DiaryItem, ImageItem
from django.core.context_processors import csrf
from django.core.mail import send_mail
from markdown import markdown
from urllib import urlopen
import datetime
import status

def get_events():
    # limit to 5
    events = DiaryItem.objects.filter(date__gt=datetime.date.today()).order_by('date', 'time');
    for e in events:
        e.datestring = e.date.strftime("%d.%m.%Y")
        e.timestring = e.time.strftime("%H:%M")
    return events

def index(request):
    context = {}
    context['state'] = status.get()
    context['events'] = get_events()
    context.update(csrf(request))
    # limit to 10 - 15
    diary_items = DiaryItem.objects.filter(date__lte=datetime.date.today()).order_by('-date', '-time');
    for di in diary_items:
        di.html = markdown(di.content)
        di.datestring = di.date.strftime("%d.%m.%Y")
        di.timestring = di.time.strftime("%H:%M Uhr")
    context['items'] = diary_items
    """
    for di in diary_items:
        image_items = ImageItem.objects.filter(diary_item=di)
        di.images = image_items
    context['items'] = diary_items
    """
    return render_to_response("index.html", context)

def location(request):
    context = {}
    context['state'] = status.get()
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
    context.update(csrf(request))
    if request.POST:
        mail = request.POST['mail_entry']
        try:
            send_mail('Subscription request', '', mail, ['devlol-join@lists.servus.at'], fail_silently=False)
        except:
            print "an error occured"
    return redirect('/')
