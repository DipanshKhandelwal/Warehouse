from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sell, name='sell'),
    url(r'^(?P<slug>[-\w\d]+)/$', views.open_pdf, name='open_pdf'),
]
