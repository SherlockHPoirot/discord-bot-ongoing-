py import discord
from discord.ext import commands
import random,os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command('codersmeme')
async def mem(ctx):
    img_name = random.choice(os.listdir("mem1"))
    with open('mem1/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.comand('notfunnymeme')
async def mim(ctx):
    img_name = random.choice(os.listdir("mim11"))
    with open('mim11/{img_name}', 'rb') as f:
        picture = discord.file(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command("tebak")
async def tebak_sampah(ctx):
   
    kategori = ["organik", "anorganik"]
    jenis_sampah = random.choice(kategori)

    
    nama_images = random.choice(os.listdir(f'sampah/{jenis_sampah}'))
    
    
    with open(f'sampah/{jenis_sampah}/{nama_images}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send("Apa jenis sampah ini?", file=picture)
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Waktu habis! Jawabannya adalah: " + nama_images)
        return

    if msg.content.lower() == jenis_sampah.lower():
        await ctx.send("Benar!")
    else:
        await ctx.send(f"Salah! Jawabannya adalah: {jenis_sampah.upper()}")

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("Token")