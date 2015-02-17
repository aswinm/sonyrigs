from data import views
from django.conf.urls import url,patterns

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^products/(?P<cid>\w+)/?$',views.products),
        url(r'^product/mudpump/?$',views.mudpump),
        url(r'^product/(?P<pid>.*)/?$',views.product),
        url(r'^product/mudpump/?$',views.product),
        url(r'^sendmail/?$',views.sendmail),
        url(r'^accessories/?$',views.accessories),
        url(r'^gallery/?$',views.gallery),
        url(r'^services/?$',views.services),
        url(r'^about/?$',views.about),
        url(r'^contact/?$',views.contact),

        )
