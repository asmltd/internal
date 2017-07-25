from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import Userdetail, Student, Onsite, Session
#
from .models import employe_details

# class UserdetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Userdetail
#         fields = ('Name', 'UserId', 'email', 'Age', 'Dob', 'Doj', 'Salary', 'Designation','ProjectName', 'Qualification', 'Teamlead', 'ClientName', 'Location','id')
#
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('Object', 'Giventime', 'ExpectedReturnTime', 'GivenTo')
#
# class OnsiteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Onsite
#         fields = ('Name', 'Entrytime', 'Exittime', 'Personmet')

class employe_detailsSerializer(serializers.ModelSerializer):
    class Meta():
        model = employe_details
        fields = "__all__"