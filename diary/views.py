from django.shortcuts import render_to_response

def calendar(request):
    return render_to_response("calendar.html")

def item(request, item_id):
    return render_to_response("item.html")

def day(request, item_id):
    return render_to_response("item.html")
