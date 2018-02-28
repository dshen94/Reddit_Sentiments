# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subreddit(models.Model):
    subreddit_name = models.CharField(max_length=25)


class Submission(models.Model):
    subreddit = models.ForeignKey(Subreddit)
    submission_title = models.TextField()
    submission_id = models.CharField(max_length=15)


class Comment(models.Model):
    submission = models.ForeignKey(Submission)
    comment_id = models.CharField(max_length=15, null=True)
    comment_text = models.TextField()


class Sentiment(models.Model):
    sentiment_id = models.UUIDField()
    comment = models.OneToOneField(Comment)
    positive = models.IntegerField()
    negaive = models.IntegerField()
    neutral = models.IntegerField()
