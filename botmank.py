import discord
import praw
import random
import os
import smtplib

discordClient = discord.Client()

@discordClient.event
async def on_ready():
    print("{0.user} is on duty!".format(discordClient))


@discordClient.event
async def on_message(message):
    if message.author == discordClient.user:
        return

    if message.content.startswith("mank hello"):
        await message.channel.send("heyy")

    if message.content.startswith("mank mail"):
        msg = message.content
        indexOfAt = int(msg.index("@"))
        indexOfMailID = 0
        for i in range(indexOfAt,0, -1):
            if msg[i] == " ":
                indexOfMailID = i
                break
        mailID = msg[indexOfMailID:(len(msg))]
        server = smtplib.SMTP_SSL("smtp.gmail.com")
        server.login("danteramone76@gmail.com", os.getenv("GMAILPASS"))
        server.sendmail("danteramone76@gmail.com", mailID, "botmank sent you an email!")
        await message.channel.send("Done!")

    if message.content.startswith("mank ping"):
        await message.channel.send("pong! I'm awake")

    if message.content.startswith("mank help"):
      await message.channel.send("botmank is a discord bot that responds to messages starting with mank. I'll be gradually adding music, role management, quirky replies and other functionality. It has these basic commands right now -\n\t**ping** - responds if online\n\t**hello** - responds with heyy\n\t**meme** - sends a random meme from r/memes hot 100\n\t**joke** - sends a lame joke from r/jokes hot 100")

    if message.content.startswith("mank meme"):
        reddit = praw.Reddit(
        client_id = os.getenv("REDDITID"),
        client_secret=os.getenv("REDDITPASS"),
        user_agent="botmank")
        url = []
        for submission in reddit.subreddit("memes").hot(limit=100):
            url.append(submission.url)
        list1 = range(1, 100, 1)
        choice = int(random.choice(list1))
        await message.channel.send(url[choice])

    if message.content.startswith("mank joke"):
        reddit = praw.Reddit(
        client_id = os.getenv("PRAWID"),
        client_secret=os.getenv("PRAWPASS"),
        user_agent="botmank")
        jokes = []
        for submission in reddit.subreddit("jokes").hot(limit=100):
            jokes.append(submission.title+submission.selftext)
        list1 = range(1, 100, 1)
        choice = int(random.choice(list1))
        await message.channel.send(jokes[choice])

discordClient.run(os.getenv("TOKEN"))
