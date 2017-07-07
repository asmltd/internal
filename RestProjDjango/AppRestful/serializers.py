from rest_framework import serializers
from .models import Userdetail, Student, Onsite

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetail
        fields = ('Name', 'UserId', 'email', 'Age', 'Dob', 'Doj', 'Salary', 'Designation','ProjectName', 'Qualification', 'Teamlead', 'ClientName', 'Location')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('Object', 'Giventime', 'ExpectedReturnTime', 'GivenTo')

class OnsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onsite
        fields = ('Name', 'Entrytime', 'Exittime', 'Personmet')