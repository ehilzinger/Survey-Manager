"""
Models for handling realtime communications.
"""
from django.db import models
from datetime import timezone, datetime

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, db_index=True)
