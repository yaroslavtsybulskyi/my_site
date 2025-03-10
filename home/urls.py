from django.urls import path, re_path

from .views import home_view, about_view, contact_view, post_view, profile_view, event_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    re_path(r'^post/(?P<id>\d+)/$', post_view, name='post'),
    re_path(r'^profile/(?P<username>[a-zA-Z0-9]+)/$', profile_view, name='profile'),
    re_path(r'^event/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', event_view, name='event'),
]