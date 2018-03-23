from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListCreateTvGuide.as_view(), name='tvguide_list'),
    url(r'^(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyTvGuide.as_view(),
        name='tvguide_detail'),
    url(r'^(?P<tvguide_pk>\d+)/channels/$',
        views.ListCreateChannel.as_view(),
        name='channel_list'),
    url(r'^(?P<tvguide_pk>\d+)/channels/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyChannel.as_view(),
        name='channel_detail'),
]
