from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^todo/(?P<id>\d+)/$', views.todo_item, name='todo_item'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/list/$', views.todo_list, name='todo_list'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^todo/(?P<id>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^$', views.todo_home, name='todo_home'),
    url(r'^todo/(?P<id>\d+)/delete/$', views.todo_delete, name='todo_delete'),
    url(r'^todo/(?P<id>\d+)/complete/$', views.todo_complete, name='todo_complete'),
]
