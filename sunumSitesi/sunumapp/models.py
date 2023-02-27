from django.db import models

class Message(models.Model):
    isim = models.CharField(max_length=200)
    yorum = models.TextField()