#!/usr/bin/python
import argparse
import discord
import asyncio
import os

from commands.attendance import print_attendance, generate_post_out

# Constants
BOT_NAMES = [
    "Daddybot",
    "Fupabot",
    "Harambot 🍌",
    "Riggbot",
    "김정은",
    "Daddybot-dev",
    "Fupabot-Dev",
    "Harambot-Dev",
    "Riggbot-Dev",
    "김정은-Dev"
]

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
    if message.author.name in BOT_NAMES:
        pass
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, 'I\'m a fuckboy.')
    # Print the upcoming post outs.
    elif message.content.startswith('!attendance'):
        await print_attendance(client, message)
    # Generate a post out event.
    elif message.content.startswith('!postout') or message.content.startswith('!late') or message.content.startswith('!absent'):
        await generate_post_out(client, message)

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
        client.run(os.environ['ATTENDANCE_BOT_PRODUCTION_TOKEN'])
    else:
        print("RIP in peace.")
