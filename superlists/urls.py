from django.conf.urls import include, url
from django.contrib import admin
from django.urls import re_path
from lists.views import home_page

urlpatterns = [
    re_path(r'^$', home_page, name='home'),
    url(r'^lists/the-only-list-in-the-world/$', 'lists.views.view_list',
        name='view_list'
    ),
]