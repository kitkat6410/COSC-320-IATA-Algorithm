import csv
import pandas as pd
import datetime as dt
from pmaw import PushshiftAPI

api = PushshiftAPI()

before = int(dt.datetime(2024,2,1,0,0).timestamp())
after = int(dt.datetime(2023,1,1,0,0).timestamp())

with open('C:\\Users\\beckc\\OneDrive - The University Of British Columbia\\UBC\\Year3\\Sem2\\COSC_320\\Project\\aviation_comments_2023.csv', 'w+', newline='',encoding="utf-8") as file:
    submissions = api.search_comments(subreddit='aviation', size=100000, until=before, since=after)
    writer = csv.writer(file)
    writer.writerow(["entry","link","isComment"])
    for post in submissions:
        writer.writerow([post['title'],"https://www.reddit.com" + post['permalink'],False])



""" this is how to get comments with PRAW library
reddit = praw.Reddit(client_id='9X68iQOOEZgXEYEKWVdeaw', client_secret='ABB9zyPVIQYfN6xJhKHE8-PtrIurGg', user_agent='aviation_scraper')
all_posts = reddit.subreddit('aviation').top(time_filter="all", limit = None)

with open('C:\\Users\\beckc\\OneDrive - The University Of British Columbia\\UBC\\Year3\\Sem2\\COSC_320\\Project\\test_reddit_posts.csv', 'w+', newline='',encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["entry","link","isComment"])
    for post in all_posts:
        writer.writerow([post.title,"https://www.reddit.com" + post.permalink,False])
"""

print("done")