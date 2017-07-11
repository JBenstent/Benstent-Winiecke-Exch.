from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_page$', views.login_page, name="loginpage"),
    url(r'^register$',views.register, name='registerpage'),
    url(r'^logout$', views.logout, name="logout"),

]
