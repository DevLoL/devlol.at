from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$',                                                                      'devlol.views.index'),

    # Static Stuff
    url(r'^location/$',                                                             'devlol.views.location'),
    url(r'^projects/$',                                                             'devlol.views.projects'),
    url(r'^members/$',                                                              'devlol.views.members'),
    url(r'^join/$',                                                                 'devlol.views.join'),
    url(r'^monitoring/$',                                                           'devlol.views.monitoring'),
    url(r'^equipment/$',                                                            'devlol.views.equipment'),
    url(r'^mail/$',                                                                 'devlol.views.mail'),

    # Diary Stuff
    url(r'^diary/$',                                                                'devlol.views.index'),
    url(r'^diary/event/(?P<event_id>[0-9]+)/$',                                     'diary.views.item'),
    url(r'^diary/(?P<day>[0-9]{2})-(?P<month>[0-9]{2}-(?P<year>[0-9]{4}))/$',       'diary.views.day'),

    # Admin Stuff
    url(r'^admin/', include(admin.site.urls)),
)
