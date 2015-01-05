from django.shortcuts import render_to_response
from diary.models import DiaryItem, ImageItem
from django.core.context_processors import csrf
from django.core.mail import send_mail
from markdown import markdown
import datetime
import status

context = {}
context['state'] = status.get()
context['events'] = DiaryItem.objects.filter(date__gt=datetime.date.today()).order_by('date', 'time');

def index(request):
    context.update(csrf(request))
    diary_items = DiaryItem.objects.filter(date__lte=datetime.date.today()).order_by('-date', '-time');
    for di in diary_items:
        di.html = markdown(di.content)
    context['items'] = diary_items
    """
    for di in diary_items:
        image_items = ImageItem.objects.filter(diary_item=di)
        di.images = image_items
    context['items'] = diary_items
    """
    return render_to_response("index.html", context)

def location(request):
    context.update(csrf(request))
    return render_to_response("location.html", context)

def projects(request):
    context.update(csrf(request))
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
        return HttpResponseRedirect("/mail/")
    return render_to_response("mail.html", context)
