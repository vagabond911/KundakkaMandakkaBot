import praw
import config
import os
import random
import time

def bot_login():
    rlogin = praw.Reddit(username = config.username, password = config.password,
                client_id = config.client_id, client_secret=config.client_secret,
                user_agent = "Kundakka Mandakka Bot v1.2")
    return rlogin

def run_bot(rlogin, comments_replied_to):
    for comment in rlogin.inbox.mentions(limit=25):
        if comment.id not in comments_replied_to:
            comment.reply(getrandom_comment()+"\n"+"This is an automated comment from a bot!")
            comments_replied_to.append(comment.id)
        else:
            print("Comment Replied")

        with open("comments_replied_to.txt", "a") as f:
            f.write(comment.id + "\n")

def getrandom_comment():
    with open("dialogues", "r") as f:
        insults = f.read()
        insults = insults.split("\n")
    return random.choice(insults)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to


rlogin = bot_login()


comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(rlogin, comments_replied_to)
    time.sleep(7200)

