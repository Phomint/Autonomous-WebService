from django.conf.urls import url, include
from autonomo.views import AutonomoList, AutonomoView
from servico.views import ServicoList, ServicoView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^autonomos/$', AutonomoList.as_view(), name='autonomos'),
    url(r'^autonomos/(?P<pk>\d+)/$', AutonomoView.as_view(), name='get_autonomo'),
    url(r'^servicos/$', ServicoList.as_view(), name='servico'),
    url(r'^servicos/(?P<pk>\d+)/$', ServicoView.as_view(), name='get_servico'),
    url(r'^', include('rest_auth.urls')),
    url(r'^registrar/', include('rest_auth.registration.urls'))
]
