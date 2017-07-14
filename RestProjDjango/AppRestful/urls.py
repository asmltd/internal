from rest_framework import routers
from .views import it_deskViewSet, UserdetailViewSet, OnsiteViewSet, SessionViewSet
from django.conf.urls import url, include
from django.contrib import admin
from .views import *

router = routers.DefaultRouter()
router.register(r'api/it_desk', it_deskViewSet)
router.register(r'api/Userdetails', UserdetailViewSet)
router.register(r'api/Onsites', OnsiteViewSet)
router.register(r'api/Sessions', SessionViewSet)

urlpatterns = [
    url(r'^accounts/login/$', signin, name='login'),
    url(r'^$', index, name='login'),
    url(r'^accounts/logout/$', signout, name='logout'),
    #url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]

urlpatterns += router.urls



