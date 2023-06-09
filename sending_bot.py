import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pyautogui as pg
import os

load_dotenv()
discord_token = os.getenv('SendingBot_token')

# Using readlines()
prompt_file = open('output_prompts.txt', 'r')
prompts = prompt_file.readlines()

prompt_counter = 0

load_dotenv()
client = commands.Bot(command_prefix="*", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot connected")


@client.event
async def on_message(message):
    global prompt_counter

    msg = message.content
    print(message)

    while prompt_counter < len(prompts):
        # Start Automation by typing "automation" in the discord channel
        if msg == 'automation':
            time.sleep(2)
            pg.press('tab')
            for i in range(1):
                time.sleep(0.5)
                pg.write('/imagine')
                time.sleep(0.8)
                pg.press('tab')
                pg.write(prompts[prompt_counter])
                time.sleep(0.5)
                pg.press('enter')
                time.sleep(0.3)
                prompt_counter += 1

        # continue Automation as soon Midjourney bot sends a message with attachment.
        for attachment in message.attachments:
            time.sleep(0.5)
            pg.write('/imagine')
            time.sleep(0.8)
            pg.press('tab')
            pg.write(prompts[prompt_counter])
            time.sleep(0.5)
            pg.press('enter')
            time.sleep(0.3)
            prompt_counter += 1

    # Add this line to process commands and events properly
    # await client.process_commands(message)
    quit()

client.run(discord_token)
