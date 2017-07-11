from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Userdetail, Student, Onsite, Session

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetail
        fields = ('Name', 'UserId', 'email', 'Age', 'Dob', 'Doj', 'Salary', 'Designation','ProjectName', 'Qualification', 'Teamlead', 'ClientName', 'Location','id')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('Object', 'Giventime', 'ExpectedReturnTime', 'GivenTo')

class OnsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onsite
        fields = ('Name', 'Entrytime', 'Exittime', 'Personmet')

class SessionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Session
        fields = "__all__"