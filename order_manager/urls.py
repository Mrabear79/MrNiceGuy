from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
     url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
     url(r'^$', views.home, name='home'),
     url(r'^product/(?P<id>\d+)/$', views.product_item, name='item'),
     url(r'^product/list/$', views.product_list, name='products'),
     url(r'^order/$', views.order_form, name='order_form'),
]
