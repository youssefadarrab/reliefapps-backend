from django.conf.urls import url
from reliefapp import views

urlpatterns=[
    url(r'^history/$',views.historyApi),
    url(r'^history/([0-9]+)$',views.historyApi),
    url(r'^bookmark/$',views.bookmarkApi),
    url(r'^bookmark/([0-9]+)$',views.bookmarkApi)
]
