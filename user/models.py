from django.db import models
from django.utils import timezone
import hashlib

class User(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(unique=True, max_length=250)
    password = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def get_userid(self):
        return self.userid

    def get_useridx(self):
        return self.id

    def get_userpassword(self):
        return self.password


    def __str__(self):
        return self.userid
