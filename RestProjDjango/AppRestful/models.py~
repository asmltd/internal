from __future__ import unicode_literals
from rest_framework import serializers
from django.db import models

# Create your models here.

class Userdetail(models.Model):
    
    Name = models.CharField(max_length=50)
    Id =  models.IntegerField()
    email = models.CharField(max_length=50)
    Age = models.IntegerField()
    Dob = models.DateField()
    Doj = models.DateField()

    class Meta:
        #verbose_name = "Userdetail"
        #verbose_name_plural = "Userdetails"
        db_table = 'tableuser'

    def __unicode__(self):
        return '%s %d %s %d %s %s' % (self.Name, self.Id, self.email, self.Age, self.Dob, self.Doj)
         #return self.Name

class Student(models.Model):
    Object = models.IntegerField()
    Giventime = models.DateTimeField()
    ExpectedReturnTime = models.DateTimeField()
    GivenTo = models.ForeignKey(Userdetail, on_delete=models.CASCADE)

    #serdetail = models.ForeignKey(Userdetail)

    class Meta:
       # verbose_name = "Student"
       # verbose_name_plural = "Students"
         db_table = 'tablestudent'

    def __unicode__(self):
        return '%d' % (self.Object)
