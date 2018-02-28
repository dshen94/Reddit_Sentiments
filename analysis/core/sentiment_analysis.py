from nltk.sentiment.vader import SentimentIntensityAnalyzer
from core.models import Comment


def run_comment_analysis():
    comments = Comment.objects.all()
