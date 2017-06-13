from __future__ import unicode_literals
from rest_framework import serializers
from django.db import models

# Create your models here.

class Userdetail(models.Model):
    
    Name = models.CharField(max_length=50)
    Id =  models.IntegerField()
    email = models.CharField(max_length=50)

    class Meta:
        #verbose_name = "Userdetail"
        #verbose_name_plural = "Userdetails"
        db_table = 'tableuser'

    def __unicode__(self):
        return '%s %d %s' % (self.Name, self.Id, self.email)
         #return self.Name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #serdetail = models.ForeignKey(Userdetail)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
