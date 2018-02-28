import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from core.models import Comment, Sentiment


def run_comment_analysis(comment):
    sid = SentimentIntensityAnalyzer()

    body_text = comment.comment_text
    sentences = sent_tokenize(body_text)
    sentiment_total = {'compound': 0, 'positive': 0, 'neutral': 0, 'negative': 0}

    for sentence in sentences:
        scores = sid.polarity_scores(sentence)
        sentiment_total['compound'] += scores['compound']
        sentiment_total['positive'] += scores['pos']
        sentiment_total['negative'] += scores['neg']
        sentiment_total['neutral'] += scores['neu']

    sent_count = len(sentences)
    sentiment_kwargs = {'comment': comment,
                        'compound': (sentiment_total['compound']/sent_count),
                        'positive': (sentiment_total['positive']/sent_count),
                        'negative': (sentiment_total['negative']/sent_count),
                        'neutral': (sentiment_total['neutral']/sent_count)}

    #create Sentiment model object
    sentiment = Sentiment(**sentiment_kwargs)
    sentiment.save()

    print "analysis complete for comment {}".format(comment.comment_id)
    return