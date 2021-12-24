import discord
import json

from discord_slash import cog_ext , SlashContext
from discord.ext import commands

class Prefix_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Prefix_cog Loaded Succesfully.')

    @commands.command()
    async def setprefix(self , ctx , prefix):
        with open("prefixes.json" , "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json" , "w") as f:
            json.dump(prefixes , f , indent = 4)

        embed=discord.Embed(title="You have change the Bot prefix to" , description=f"\n`{prefix}`" , color=discord.Color.blurple())

        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="setprefix" , description="change prefix")
    async def setprefix(self , ctx , prefix):
        with open("prefixes.json" , "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json" , "w") as f:
            json.dump(prefixes , f , indent = 4)

        embed=discord.Embed(title="You have change the Bot prefix to" , description=f"\n`{prefix}`" , color=discord.Color.blurple())

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Prefix_cog(bot))