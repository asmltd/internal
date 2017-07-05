from rest_framework import serializers
from .models import Userdetail, Student

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetail
        fields = ('Name', 'UserId', 'email', 'Age', 'Dob', 'Doj')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('Object', 'Giventime', 'ExpectedReturnTime', 'GivenTo')
