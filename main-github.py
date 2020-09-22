import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup as BS 
import requests 

client = commands.Bot(command_prefix = "!")
token = ('YOUR TOKEN HERE')
client.remove_command('help')

country = "YOUR COUNTRY HERE"

@tasks.loop(seconds=600)
async def corona_cases():
    url = f"https://www.worldometers.info/coronavirus/country/{country}/"
    data = requests.get(url)
    soup = BS(data.text, 'html.parser')
    cases = soup.find_all("div", class_ = "maincounter-number")
    total = cases[0].text 
    total = total[1 : len(total) - 2] 
    channellatency = client.get_channel(THE ID OF YOUR FIRST VC HERE)
    await channellatency.edit(name=f"🦠| {total} Cases")

@tasks.loop(seconds=600)
async def corona_survives():
    url = f"https://www.worldometers.info/coronavirus/country/{country}/"
    data = requests.get(url)
    soup = BS(data.text, 'html.parser')
    cases = soup.find_all("div", class_ = "maincounter-number")
    recovered = cases[2].text 
    recovered = recovered[1 : len(recovered) - 1] 
    channellatency = client.get_channel(THE ID OF YOUR SECOND VC HERE)
    await channellatency.edit(name=f"👼| {recovered} Recovereds")

@tasks.loop(seconds=600)
async def corona_deaths():
    url = f"https://www.worldometers.info/coronavirus/country/{country}/"
    data = requests.get(url)
    soup = BS(data.text, 'html.parser')
    cases = soup.find_all("div", class_ = "maincounter-number")
    deaths = cases[1].text 
    deaths = deaths[1 : len(deaths) - 1] 
    channellatency = client.get_channel(THE ID OF YOUR THIRD VC HERE)
    await channellatency.edit(name=f"💀| {deaths} Deaths")

@client.event
async def on_ready():
    print("The bot is ready :")
    print("Connected at :")
    print(client.user.name)
    print(client.user.id)
    print("Copyright Coronavirus© 2020 LTD All right reserved.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Coronavirus"))

    corona_deaths.start()
    corona_cases.start()
    corona_survives.start()

client.run(token)