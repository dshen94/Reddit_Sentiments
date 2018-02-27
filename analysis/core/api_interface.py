import praw
from .models import Subreddit, Submission, Comment

def get_reddit_client():
    client = praw.Reddit(client_id='f2PnncgffkjTvQ',
                         client_secret='Rbjw4fLaEEH4mg8UCPKfAg26d1M',
                         username='klaytheistic',
                         password='ripteamtweets',
                         user_agent='Analyzing popular subredditsentiments by u/klaytheistic')

    return client


def add_popular_subreddits():
    client = get_reddit_client()
    popular_subs = client.subreddits.popular()

    for sub in popular_subs:
        _, _ = Subreddit.objects.get_or_create(subreddit_name=sub.display_name)
    return


def add_top_submissions(subreddit_name, limit=100):
    client = get_reddit_client()
    subreddit = client.subreddit(subreddit_name)
    for post in subreddit.top(limit):
        _, _ = Submission.objects.create_or_get(subreddit=subreddit,
                                                submission_title=post.title,
                                                submission_id=post.id)
    return


def add_comments(submission_id):
    client = get_reddit_client()
    submission_model = Submission.objects.get()
    submission = client.submission(id=submission_id)

    for comment in submission.comments.list():
        submission.comments.replace_more(limit=0)
        _, _ = Comment.objects.get_or_create(submission=submission_model, comment_text=comment.comment_text)
    return

