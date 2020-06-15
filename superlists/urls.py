from django.conf.urls import include, url
from django.contrib import admin
from django.urls import re_path
from lists.views import home_page

urlpatterns = [
    re_path(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    re_path(r'^(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
    re_path(r'^new$', 'lists.views.new_list', name='new_list'),
]