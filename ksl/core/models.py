from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published (or NULL if unapproved)')
    date_updated = models.DateTimeField('date updated')

class Keyword(models.Model):
    text = models.CharField(max_length=128)
    date_updated = models.DateTimeField('date updated')

class WordToKeyword(models.Model):
    word = models.ForeignKey(Word)
    keyword = models.ForeignKey(Keyword)
    date_updated = models.DateTimeField('date updated')

class Video(models.Model):
    filename = models.CharField(max_length=512)
    pub_date = models.DateTimeField('date published')
    date_updated = models.DateTimeField('date updated')

class WordToVideo(models.Model):
    word = models.ForeignKey(Word)
    video = models.ForeignKey(Video)
    date_updated = models.DateTimeField('date updated')
