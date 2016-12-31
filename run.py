#!/usr/bin/python
import argparse

import discord
import asyncio
from commands.attendance import print_attendance, generate_post_out

# Development Constants
DEV_BOT_NAME = "Riggbot-Dev"
DEV_BOT_KEY = "MjY0MTIyNzMzMTAzODA4NTEy.C0b_Gg.cwC9mmjMfJcOc_6tEBeIemigiHA"

# Production Constants
PRODUCTION_BOT_NAME = "Riggbot"
PRODUCTION_BOT_KEY = "MjY0MTIyNTg5Mjg1MzE4NjU2.C0b_Wg.pg7X_dSFEetlSrBwk-WHMA4YnW0"

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
        client.run(DEV_BOT_KEY)
    elif args.prod:
        client.run(PRODUCTION_BOT_KEY)
    else:
        print("RIP in peace.")
