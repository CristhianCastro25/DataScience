from django.conf.urls import url, include
from django.contrib import admin

from . views import index, list_review, add_review

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^list/$', list_review, name="list_review"),
    url(r'^add/$', add_review, name="add_review"),
]
