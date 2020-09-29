# by John Hadden
import praw
import random
import time  # the modules needed for the script

# the code to access praw and login to reddit
reddit = praw.Reddit(client_id='LsDR_-EEXqr-xA',
                     client_secret='UIzmQDXm4uG-_SIjGc1PBdvDw78',
                     user_agent='reddit bot for a client on 5iverr',
                     username='Interesting-Parsnip4',
                     password='SwagKing69', )
subreddits = ['technology', 'software', 'windows', 'Windows10', 'email', 'outlook', 'GMail',
              'techsupport', 'softwareachitecture', 'android', 'mac','microsoftsoftwareswap', 'windowsinsiders', 'linux', 'tech']
while True:
    int = random.randint(0, len(subreddits) - 1)
    subreddit = reddit.subreddit(subreddits[int])  # declares the subreddit that you want to do this on
    subreddit.submit('Feedback on MailBird with email tracking',
                     'https://www.reddit.com/r/windows/comments/j1u5uj/we_are_live_on_product_hunt_and_would_appreciate/')
    time.sleep(300)