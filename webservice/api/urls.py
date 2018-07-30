from django.conf.urls import url
from autonomo.views import AutonomoList, AutonomoView
from servico.views import ServicoList, ServicoView
from usuario.views import LoginView, LogoutView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^autonomos/$', AutonomoList.as_view(), name='autonomos'),
    url(r'^autonomos/(?P<pk>\d+)/$', AutonomoView.as_view(), name='get_autonomo'),
    url(r'^servicos/$', ServicoList.as_view(), name='servico'),
    url(r'^servicos/(?P<pk>\d+)/$', ServicoView.as_view(), name='get_servico'),
]
