import discord , os , random
from oh-no import sifre,ZOR
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam!")
@bot.command()
async def sa(ctx):
    await ctx.send("aleyküm selam!")
@bot.command()
async def selamınaleyküm(ctx):
    await ctx.send("aleyküm selam!")
@bot.command()
async def teşşekür(ctx):
    await ctx.send("no problem!")
@bot.command()
async def teşşekürler(ctx):
    await ctx.send("no problem!")
@bot.command()
async def sifre(ctx):
    passs = "shhh saklayın! " + str(sifre(ZOR, 12))
    await ctx.send(passs)
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def PİNG(ctx):
    await ctx.send('POOOOONG')
@bot.command()
async def oneplusone(ctx):
    await ctx.send('ÇOK KOMİK!!')
@bot.command()
async def minibombardıman(ctx):
    for i in range(10):
        await ctx.send('MATEMATİKTEN KAÇ ALDINNNN? @everyone')
@bot.command()
async def bombardıman(ctx):
    for i in range(30):
        await ctx.send('MATEMATİKTEN KAÇ ALDINNNN? @everyone')
@bot.command()
async def görüşürüzmatematik(ctx):
    await ctx.send('3,1415192...')
    await bot.close()
@bot.command
async def topla(ctx,a1=0,a2=0):
    ctx.send(a1+a2)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("AAA"))
    with open(f"AAA/{img_name}","rb")as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
#sana token moken yok!

import requests,aiohttp

async def get_cat_image_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()
            return data[0]['url']  # 'url' anahtarına doğrudan erişim

@bot.command(name='cat')
async def cat(ctx):
    image_url = await get_cat_image_url()
    await ctx.send(image_url)




def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

async def get_element_image_url():
    url = 'https://periodic-table-elements-info.herokuapp.com/elements'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()
            return data[0]['url']  # 'url' anahtarına doğrudan erişim

@bot.command(name='element')
async def element(ctx):
    image_url = await get_element_image_url()
    await ctx.send(image_url)









bot.run("")
