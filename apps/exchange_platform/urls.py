from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
<<<<<<< HEAD
=======
    url(r'^$', views.index),
    url(r'^login_page$', views.login_page, name="loginpage"),
    url(r'^register$',views.register, name='registerpage'),
    url(r'^logout$', views.logout, name="logout"),
>>>>>>> 63a8fe92f81eb590b80f6f35c1265fcbf6769994


    url(r'^async_include/', include('async_include.urls', namespace="async_include")),
    url(r'^$', TemplateView.as_view(template_name='exchange_platform/index.html'), name='home'),
    url(r'^football$', TemplateView.as_view(template_name='exchange_platform/football.html'), name='football'),
    url(r'^baseball$', views.baseball)
]

# urlpatterns = [
#     url(r'^$', views.index),
#
# ]
