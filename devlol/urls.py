from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'devlol.views.index'),

    # Static Stuff
    url(r'^location/$', 'devlol.views.location'),
    url(r'^mail/$',     'devlol.views.mail'),

    # Diary Stuff
    url(r'^diary/$',                            'devlol.views.index'),
    url(r'^diary/event/(?P<event_id>[0-9]+)/$', 'diary.views.item'),

    # API Stuff
    url(r'^api/events$', 'devlol.views.events'),
    url(r'^api/ical$', 'devlol.views.ical'),

    # Admin Stuff
    url(r'^admin/', include(admin.site.urls)),
)
