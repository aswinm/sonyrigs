from data import views
from django.conf.urls import url,patterns

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^sendmail/?$',views.sendmail),
        )
