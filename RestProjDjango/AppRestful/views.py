from django.shortcuts import render
from rest_framework import viewsets
from .models import Userdetail, Student
from .serializers import UserdetailSerializer, StudentSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserdetailViewSet(viewsets.ModelViewSet):
    queryset = Userdetail.objects.all()
    serializer_class = UserdetailSerializer
