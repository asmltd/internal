from rest_framework import routers

from django.conf.urls import url, include
from django.contrib import admin
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^accounts/login/$', signin, name='login'),
    url(r'^$', index, name='login'),
    url(r'^accounts/logout/$', signout, name='logout'),

]

urlpatterns += router.urls



