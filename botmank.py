import discord
import praw
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} is on duty!".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("mank hello"):
        await message.channel.send("heyy")

    if message.content.startswith("mank fuckoff"):
        await message.channel.send("you fuckoff!")

    if message.content.startswith("mank ping"):
        await message.channel.send("pong! I'm awake")

    if message.content.startswith("mank meme"):
        reddit = praw.Reddit(client_id=os.getenv("REDDITID"),
                             client_secret=os.getenv("REDDITPASS"),
                             user_agent="botmank")
        url = []
        for submission in reddit.subreddit("memes").hot(limit=100):
            url.append(submission.url)
        list1 = range(1, 100, 1)
        choice = int(random.choice(list1))
        await message.channel.send(url[choice])

    if message.content.startswith("mank joke"):
        reddit = praw.Reddit(client_id=os.getenv("REDDITID"),
                             client_secret=os.getenv("REDDITPASS"),
                             user_agent="botmank")
        url = []
        for submission in reddit.subreddit("jokes").hot(limit=100):
            url.append(submission.url)
        list1 = range(1, 100, 1)
        choice = int(random.choice(list1))
        await message.channel.send(url[choice])
        
client.run(os.getenv("TOKEN"))
