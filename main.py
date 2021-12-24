import discord
import os
import json

from itertools import cycle
from discord.ext import commands , tasks

TOKEN="ODY1NDU0NzExMjMzNzA4MDMz.YPEPgg.-4WMoy5D3NOlUjX0CmWsh-r_194"

################################################

def get_prefix(bot , message):
    with open("prefixes.json" , "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

################################################

bot = commands.Bot(command_prefix= (get_prefix) , case_insensitive=True, description="Testing propose only")

bot.remove_command("help")

################################################

@bot.event
async def on_guild_join(guild):
    with open("prefixes.json" , "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "="

    with open("prefixes.json" , "w") as f:
        json.dump(prefixes , f , indent = 4)

@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json" , "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json" , "w") as f:
        json.dump(prefixes , f , indent = 4)

################################################

status = cycle(
    ['=help','=play','In Devolopment'])

@bot.event
async def on_ready():
    change_status.start()
    print(f"{bot.user.name} is ready to use".format(bot))

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

################################################

for filename in os.listdir('./discord_bot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

################################################

bot.run(TOKEN)