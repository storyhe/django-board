from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):

    id = models.AutoField(primary_key=True)
    writer_id = models.IntegerField(null=True)
    board_id = models.IntegerField(null=False, default=0)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Board(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    isUsed = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name