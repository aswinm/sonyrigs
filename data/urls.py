from data import views
from django.conf.urls import url,patterns

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^products/(?P<cid>\w+)/?$',views.products),
        url(r'^product/(?P<pid>.*)/?$',views.product),
        url(r'^sendmail/?$',views.sendmail),
        url(r'^gallery/?$',views.gallery),

        )
