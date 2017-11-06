from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.about_us, name='about_us'),
]
