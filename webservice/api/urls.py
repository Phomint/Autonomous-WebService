from django.conf.urls import url
from autonomo.views import AutonomoList, AutonomoView
from servico.views import ServicoList, ServicoView
from usuario.views import UsuarioList, UsuarioView

urlpatterns = [
    url(r'^autonomos/$', AutonomoList.as_view(), name='autonomos'),
    url(r'^autonomos/(?P<pk>\d+)/$', AutonomoView.as_view(), name='get_autonomo'),
    url(r'^servicos/$', ServicoList.as_view(), name='servico'),
    url(r'^servicos/(?P<pk>\d+)/$', ServicoView.as_view(), name='get_servico'),
    url(r'^usuarios/$', UsuarioList.as_view(), name='usuario'),
    url(r'^usuarios/(?P<pk>\d+)/$', UsuarioView.as_view(), name='get_usuario'),
]
