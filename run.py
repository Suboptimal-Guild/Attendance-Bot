#!/usr/bin/python
import argparse
import discord
import asyncio
import os

from commands.attendance import print_attendance, generate_post_out

# Development Constants
<<<<<<< HEAD
DEV_BOT_NAME = "Riggbot-Dev"

# Production Constants
PRODUCTION_BOT_NAME = "Riggbot"
=======
DEV_BOT_NAME = "김정은-Dev"
DEV_BOT_KEY = "MjY0NjEzMjYxMzM1NDYxODg4.C0jH0w.JgIQpBMbBzPULupWpETORGUTGtI"

# Production Constants
PRODUCTION_BOT_NAME = "김정은"
PRODUCTION_BOT_KEY = "MjY0NjEyNzE4MDc2NjI0ODk3.C0jHUg.Pc3iVPh38-hyOTfH3OCinJp6q6M"
>>>>>>> 92f8861a5d25446c67d6805c3b5525ee03893702

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): # placeholder "bookmarks"
    # also we want to post messages in the channe lwhere the user asked, but
    # if possible make the message only viewable to them kinda like the default bot can do
    if message.author.name == DEV_BOT_NAME or message.author.name == PRODUCTION_BOT_NAME:
        pass
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, 'I\'m a fuckboy.')
    elif message.content.startswith('!epgp export') and is_officer(message.author):
        await update_EPGP(client, message)
    elif message.content.startswith('!epgp leaderboard'):
        await print_EPGP_leaderboard(client, message)
    elif message.content.startswith('!epgp'):
        await print_EPGP(client, message)

if __name__ == "__main__":
    '''
    Add two mutually exclusive commands, where one of the two is required for the
    script to run.
    '''
    parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d','--dev',help="Run the bot in development mode.",action="store_true")
    group.add_argument('-p', '--prod',help="Run the bot in production mode.",action="store_true")
    args = parser.parse_args()

    client.accept_invite('https://discord.gg/mM5fXCe')

    if args.dev:
        client.run(os.environ['ATTENDANCE_BOT_DEVELOPMENT_TOKEN'])
    elif args.prod:
<<<<<<< HEAD
        client.run(os.environ['ATTENDANCE_BOT_PRODUCTION_TOKEN'])
=======
        client.run(PRODUCTION_BOT_KEY)
>>>>>>> 92f8861a5d25446c67d6805c3b5525ee03893702
    else:
        print("RIP in peace.")
