from rest_framework import routers
from .views import StudentViewSet, UserdetailViewSet
from django.conf.urls import url, include
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'Userdetails', UserdetailViewSet)

urlpatterns = [
    url(r'^api/', include('rest_framework.urls')),
]

urlpatterns += router.urls

