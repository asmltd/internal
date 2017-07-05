from __future__ import unicode_literals
from rest_framework import serializers
from django.db import models

# Create your models here.

class Userdetail(models.Model):
    
    Name = models.CharField(max_length=50)
    UserId =  models.IntegerField()
    email = models.CharField(max_length=50)
    Age = models.IntegerField()
    Dob = models.DateField()
    Doj = models.DateField()

    #class Meta:
        #verbose_name = "Userdetail"
        #verbose_name_plural = "Userdetails"
        #db_table = 'tableuser'

    def __unicode__(self):
        return '%s %d %s %d %s %s' % (self.Name, self.UserId, self.email, self.Age, self.Dob, self.Doj)
         #return self.Name

class Student(models.Model):
    Object = models.CharField(max_length=50)
    Giventime = models.DateField()
    ExpectedReturnTime = models.DateField()
    GivenTo = models.ForeignKey(Userdetail, on_delete=models.CASCADE)

    #userdetail = models.ForeignKey(Userdetail)

    #class Meta:
    #    verbose_name = "Student"
    #    verbose_name_plural = "Students"
    #    db_table = 'objects'
   
    def __unicode__(self):
       return '%s' % (self.Object)


