from django.db import models
import os
import sys










class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField(
        blank=True,
        null=True,
        help_text="date of the event"
    )
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()
    event_image = models.ImageField(upload_to="events/")

    def __str__(self):
        return self.event_name






class VideoSegments(models.Model):
    video_segment = models.FileField(upload_to="video/")
    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        related_name="video_segments"
    )

    def __str__(self):
        return self.video_segment.name


class DailyBread(models.Model):
    scripture_name = models.TextField(help_text="Bible reference")
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(help_text=" the person who wrote the passage")
    def __str__(self):
        return self.scripture_name


class EventSales(models.Model):
    Product = models.CharField(help_text=" products that we have for sale")
    description = models.TextField(help_text= "a description of the product")
    price = models.DecimalField(max_digits=3, decimal_places=2 )
    product_image = models.ImageField(upload_to="products/", blank=True)
    def __str__(self):
        return self.Product

class ChatBot(models.Model):
    input_text = models.TextField()
    chat = models.TextField()
    def __str__(self):
        return self.chat


class Pastor(models.Model):
    name = models.CharField(max_length=100)
    help_text = "person that we are praying for"
    email = models.EmailField(
        blank=True,
        help_text=" send this person a positive affirmations")
    audio_segment = models.FileField(upload_to="prayers_for_those_in_need/", blank=True)

    prayer = models.TextField(help_text="add a prayer", blank=True)
    def __str__(self):
        return self.name




class LocalScripture(models.Model):
    topic = models.CharField(max_length=100, unique=True)
    reference = models.CharField(max_length=100)
    reflection = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic


