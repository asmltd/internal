# from __future__ import unicode_literals
# from rest_framework import serializers
# from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.sessions.backends.db import SessionStore as DBStore
# from django.contrib.sessions.base_session import AbstractBaseSession
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser, Group

class employe_details(AbstractUser):
    team = models.CharField(max_length=50, default='')
    image = models.ImageField(null=True,blank=True,upload_to='user_images/')

    def json_ready(self, detailed=False):
        data = {'id': self.id,
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'image': str(self.image),
                'team': self.team if self.team else "",
                }

        if detailed:
            pass

        return data
