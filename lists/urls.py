from django.conf.urls import include, url
from django.contrib import admin
from django.urls import re_path
from lists.views import home_page

urlpatterns = [
    re_path(r'^$', 'lists.views.home_page', name='home'),
    re_path(r'^lists/(\d+)/$', 'lists.views.view_list', name='view_list'),
    re_path(r'^lists/(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
    re_path(r'^lists/new$', 'lists.views.new_list', name='new_list'),
]