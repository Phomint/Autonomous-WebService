from django.conf.urls import url
from autonomo.views import AutonomoList, AutonomoView

urlpatterns = [
    url(r'^autonomos/$', AutonomoList.as_view(), name='autonomos'),
    url(r'^autonomos/(?P<pk>\d+)/$', AutonomoView.as_view(), name='get_autonomo')
]
