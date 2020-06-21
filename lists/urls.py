from django.conf.urls import include, url
from django.contrib import admin
from lists.views import home_page, view_list, add_item, new_list

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^lists/(\d+)/$', view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$', add_item, name='add_item'),
    url(r'^lists/new$', new_list, name='new_list'),
]