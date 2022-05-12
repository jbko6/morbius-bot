import discord
from discord.ext import commands

import csv
import re
import os
from dotenv import load_dotenv

description = "Morbius incarnated as a discord bot. It's morbin time!"

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot('m!', description=description, intents=intents)

load_dotenv()

# ------------- VARIABLES -------------------------

responsesCSV = "responses.csv"
responsePairs = dict()

# csv parsing into dictionary for easy access
with open(responsesCSV, 'r') as responses:
    reader = csv.DictReader(responses)

    for row in reader:
        responsePairs[row['Keywords']] = row['Response']

# ------------- COMMANDS --------------------------

@bot.event
async def on_ready():
    print("Logged in as {0.user}, it's morbin time".format(bot))

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    for pair in responsePairs:
        match = re.search(pair, message.content)
        
        if match != None:
            print(match)
            await message.channel.send(responsePairs[pair])

# -------------------------------------------------

bot.run(os.environ['TOKEN'])