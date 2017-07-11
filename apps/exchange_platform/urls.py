from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [


    url(r'^async_include/', include('async_include.urls', namespace="async_include")),
    url(r'^$', TemplateView.as_view(template_name='exchange_platform/index.html'), name='home'),
    url(r'^football$', TemplateView.as_view(template_name='exchange_platform/football.html'), name='football'),
    url(r'^baseball$', views.baseball)
]

# urlpatterns = [
#     url(r'^$', views.index),
#
# ]
