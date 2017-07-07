from __future__ import unicode_literals
from rest_framework import serializers
from django.db import models


# Create your models here.

class Userdetail(models.Model):
    Name = models.CharField(max_length=50)
    UserId = models.IntegerField()
    email = models.CharField(max_length=50)
    Age = models.IntegerField()
    Dob = models.DateField()
    Doj = models.DateField()
    Salary = models.IntegerField()
    Designation = models.CharField(max_length=50)
    ProjectName = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=50)
    Teamlead = models.CharField(max_length=50)
    ClientName = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)

    # class Meta:
    # verbose_name = "Userdetail"
    # verbose_name_plural = "Userdetails"
    # db_table = 'tableuser'

    def __unicode__(self):
        return '%s %d %s %d %s %s %d %s %s %s %s %s %s' % (
            self.Name, self.UserId, self.email, self.Age, self.Dob, self.Doj, self.Salary, self.Designation,
            self.ProjectName, self.Qualification, self.Teamlead, self.ClientName, self.Location)
        # return self.Name


class Student(models.Model):
    Object = models.CharField(max_length=50)
    Giventime = models.DateField()
    ExpectedReturnTime = models.DateField()
    GivenTo = models.ForeignKey(Userdetail, on_delete=models.CASCADE)

    # userdetail = models.ForeignKey(Userdetail)

    # class Meta:
    #    verbose_name = "Student"
    #    verbose_name_plural = "Students"
    #    db_table = 'objects'

    def __unicode__(self):
        return '%s' % (self.Object)


class Onsite(models.Model):
    Name = models.CharField(max_length=50)
    Entrytime = models.DateField()
    Exittime = models.DateField()
    Personmet = models.ForeignKey(Userdetail, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % (self.Name)

class Session(models.Model):
        Username = models.CharField(max_length=50)
        Email = models.CharField(max_length=50)
        Userid = models.ForeignKey(Userdetail, on_delete=models.CASCADE)

        def __unicode__(self):
             return '%s' % (self.Username)
