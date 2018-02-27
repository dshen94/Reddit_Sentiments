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
    title_sentiment = models.IntegerField(null=True, blank=True)


class Comment(models.Model):
    submission = models.ForeignKey(Submission)
    comment_text = models.TextField()
    comment_sentiment = models.IntegerField(null=True, blank=True)
