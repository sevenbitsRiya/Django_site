from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^s/$', views.search, name='search'),
    url(r'^q/$', views.sort, name='sort'),
    url(r'^product_list/$', views.product_list, name='product_list'),
    #url(r'^product_filter/$', views.product_filter, name='product_filter'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    
]