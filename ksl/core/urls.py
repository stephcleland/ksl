from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^$', views.detail, name='detail'),
)
