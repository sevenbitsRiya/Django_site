from django.conf.urls import url
from . import views

app_name = 'checkout'

urlpatterns = [
    url(r'^checkout/$', views.checkout, name='checkout')
]