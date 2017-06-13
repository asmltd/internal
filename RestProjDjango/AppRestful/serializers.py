from rest_framework import serializers
from .models import Userdetail, Student

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetail
        fields = ('Name', 'Id', 'email')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
