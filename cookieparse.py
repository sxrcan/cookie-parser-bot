
import requests
import discord
from discord.ext import commands
import os
import time

intents = discord.Intents().all()
client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name="dmden file at")
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    if str(message.attachments) == "[]": 
        print('yok')
    else: 
        split_v1 = str(message.attachments).split("filename='")[1]
        filename = str(split_v1).split("' ")[0]
        if filename.endswith(".txt"): 
            await message.attachments[0].save(fp=f"salam.txt") 


            os.system(f'node parser.js salam.txt sonuc.txt')

            await message.author.send('bekle..')
            time.sleep(5)

            
            await message.author.send(file=discord.File(r'sonuc.txt'))
            time.sleep(1)
            os.system('del sonuc.txt')


print('baglandi')
client.run('tokeni gir.')


    

