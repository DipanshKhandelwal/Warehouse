from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.buy, name='buy'),
    url(r'^save/$', views.write_pdf, name='write_pdf'),
]
