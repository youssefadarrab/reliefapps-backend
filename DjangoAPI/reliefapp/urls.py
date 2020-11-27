from django.conf.urls import url
from reliefapp import views

urlpatterns=[
    url(r'^video/$', views.videoApi),
    url(r'^video/([0-9]+)$', views.videoApi)
]