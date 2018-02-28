from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
class Subreddit(models.Model):
    subreddit_name = models.CharField(max_length=25)


class Submission(models.Model):
    subreddit = models.ForeignKey('Subreddit', on_delete=models.CASCADE)
    submission_title = models.TextField()
    submission_id = models.CharField(max_length=15)


class Comment(models.Model):
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    comment_id = models.CharField(max_length=15, null=True)
    comment_text = models.TextField()


class Sentiment(models.Model):
    sentiment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.OneToOneField('Comment', on_delete=models.CASCADE)
    compound = models.IntegerField(null=True)
    positive = models.IntegerField(null=True)
    negative = models.IntegerField(null=True)
    neutral = models.IntegerField(null=True)