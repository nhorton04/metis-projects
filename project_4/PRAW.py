import praw
import pickle

'''Simple code to get comments from Reddit API'''

reddit = praw.Reddit(client_id='Hcx9WrUhRZm6Kw', client_secret='UpyC5FWWd91tpYvXBN7LjTbidWQ', user_agent='comment_DL')
psych = reddit.subreddit('psychology')


comments = []

for submission in psych.hot(limit=1000):
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments.append(comment.body)

with open('psych.pickle', 'wb') as file:
    pickle.dump(comments, file)

'''Rinse and repeat for each desired subreddit, adjusting the limit according to the amount of activity on the target subreddit. For example, Askreddit is an extremely active subreddit, so this code would return a much higher number of comments than it would for r/psychology.'''
