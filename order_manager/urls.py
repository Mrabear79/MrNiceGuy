from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
     url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
     url(r'^$', views.home, name='home'),
     url(r'^product/(?P<id>\d+)/$', views.product_item, name='item'),
     url(r'^product/list/$', views.product_list, name='products'),
     url(r'^order/$', views.order_form, name='order_form'),
    #  url(r'^strain/(?P<strain>\w+)/$', views.order_manager_order_form, name='order_manager_order_form'),
     # url(r'^price/(?P<price>\w+)/$', views.order_manager_price, name='order_manager_price'),
     # url(r'^order_manager/new/$', views.order_manager_new, name='order_manager_new'),
     # url(r'^order_manager/(?P<id>\d+)/complete/$', views.order_manager_complete, name='order_manager_complete'),
]
