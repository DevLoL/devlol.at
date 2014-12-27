from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$',                                                                      'devlol.views.home'),
    url(r'^diary/$',                                                                'diary.views.calendar'),
    url(r'^diary/event/(?P<event_id>[0-9]+)/$',                                     'diary.views.item'),
    url(r'^diary/(?P<day>[0-9]{2})-(?P<month>[0-9]{2}-(?P<year>[0-9]{4}))/$',       'diary.views.day'),

    url(r'^admin/', include(admin.site.urls)),
)
