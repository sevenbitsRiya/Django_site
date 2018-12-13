from django.conf.urls import url
from . import views

app_name = 'contact'

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    
]