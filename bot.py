import discord
from discord.ext import commands
import requests
import pyttsx3

engine = pyttsx3.init()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

rate = engine.getProperty('rate')
print (rate)                       
engine.setProperty('rate', 155)

volume = engine.getProperty('volume')
print (volume)                          
engine.setProperty('volume',2.0)

def get_weather(city: str) -> str:
    base_url = f"https://wttr.in/{city}?format=%C+%t" # Formato: descrição + temperatura
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Não foi possível obter os dados meteorológicos. Tente novamente mais tarde."

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

@bot.command()
async def start(ctx):
    await ctx.send("Eae fih, bão?")

@bot.command()
async def weather(ctx, *, city: str):   
    weather_info = get_weather(city)
    await ctx.send(f"A previsão do tempo para {city} é {weather_info}.")
    speak(f"A previsão do tempo para {city} é {weather_info}.")



bot.run("TOKEN DO BOT!")