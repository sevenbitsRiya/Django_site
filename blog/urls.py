from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('post_detail/', views.post_detail, name='post_detail'),
    url(r'^(?P<title>[-\w]+)/$', views.product_detail, name='product_detail'),   
]