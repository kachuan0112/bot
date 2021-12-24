import discord
import time
import psutil

from discord_slash import cog_ext , SlashContext
from datetime import datetime
from discord.ext import commands

class Info_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Info_cog Loaded Succesfully.')

    @commands.command(name="help" , description="See what command you can use")
    async def help(self , ctx):
        embed=(discord.Embed(title="**BOT COMMANDS**" , description="**See All Commands in here**" , color=discord.Color.blurple())
        .add_field(name='**Music Commands ! **', value="`play` , `=music (do this commands for more imformation)`",inline=False)
        .add_field(name="**Other fun commands !** " , value="`ping` , `lmao` , `lmfao`" , inline=False)
        .add_field(name="**Other Commands ! **" , value="`help` , `invite` , `server` , `bot / botinfo`" , inline=False)
        .add_field(name="Admin commands(remember give Bot also an Administrator)" , value="`mute` , `unmute` , `warn` , `setprefix`", inline=False)
        .add_field(name="NFSW" , value="`porn` , `website` , `sex`", inline=False)
        .set_footer(text="=help will show this commands. ",icon_url="https://cdn.discordapp.com/emojis/800566172600893450.gif?size=96")
        )
        await ctx.send(embed=embed) 


    @cog_ext.cog_slash(name="help" , description="See what command you can use")
    async def help(self , ctx):
        embed=(discord.Embed(title="**BOT COMMANDS**" , description="**See All Commands in here**" , color=discord.Color.blurple())
        .add_field(name='**Music Commands ! **', value="`play` , `=music (do this commands for more imformation)`",inline=False)
        .add_field(name="**Other fun commands !** " , value="`ping` , `lmao` , `lmfao`" , inline=False)
        .add_field(name="**Other Commands ! **" , value="`help` , `invite` , `server` , `bot / botinfo`" , inline=False)
        .add_field(name="Admin commands(remember give Bot also an Administrator)" , value="`mute` , `unmute` , `warn` , `setprefix`", inline=False)
        .add_field(name="NFSW" , value="`porn` , `website` , `sex`", inline=False)
        .set_footer(text="=help will show this commands. ",icon_url="https://cdn.discordapp.com/emojis/800566172600893450.gif?size=96")
        )
        await ctx.send(embed=embed) 

    @commands.command()
    async def music(self , ctx):
        embed = discord.Embed(title="**Music Commands**" , description="refer this commands below." , color=discord.Color.blurple())
        embed.add_field(name="play <url>/<songs name>" , value="For Join The Voice Call And Play Music." , inline=False)
        embed.add_field(name="loop" , value="For Loop The Music." , inline=False)
        embed.add_field(name="leave/disconnect" , value="For Leave The Channel And Stop Music." , inline=False)
        embed.add_field(name="queue" , value="For Checking The List Of Songs." , inline=False)
        embed.add_field(name="volume/vol" , value="For Set Bot Volume." , inline=False)
        embed.add_field(name="stop" , value="For Stop All Songs And Clear The List." , inline=False)
        embed.add_field(name="skip/forceskip" , value="For Skip To The Next Songs." , inline=False)
        embed.add_field(name="remove" , value="Removes A Songs From The Queue At A Given Index." , inline=False)
        embed.add_field(name="join" , value="For Join A Channel." , inline=False)
        embed.add_field(name="shuffle" , value="For Empty Queue." , inline=False)
        embed.add_field(name="Error You Will Have" , value=f"\n→If play a songs didn't join and play/no sound/didn't send embed please simply do `=leave`."  f"\n→Bot Will Be Leave In Two Hours If Nothing Have Been Play In That Moment." , inline=False)
        embed.set_footer(text="This Bot Is Program By Python" , icon_url="https://cdn.discordapp.com/emojis/889708830827626578.png?size=96")
        embed.timestamp=datetime.utcnow()
        
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(description="music command")
    async def music(self , ctx):
        embed = discord.Embed(title="**Music Commands**" , description="refer this commands below." , color=discord.Color.blurple())
        embed.add_field(name="play <url>/<songs name>" , value="For Join The Voice Call And Play Music." , inline=False)
        embed.add_field(name="loop" , value="For Loop The Music." , inline=False)
        embed.add_field(name="leave/disconnect" , value="For Leave The Channel And Stop Music." , inline=False)
        embed.add_field(name="queue" , value="For Checking The List Of Songs." , inline=False)
        embed.add_field(name="volume/vol" , value="For Set Bot Volume." , inline=False)
        embed.add_field(name="stop" , value="For Stop All Songs And Clear The List." , inline=False)
        embed.add_field(name="skip/forceskip" , value="For Skip To The Next Songs." , inline=False)
        embed.add_field(name="remove" , value="Removes A Songs From The Queue At A Given Index." , inline=False)
        embed.add_field(name="join" , value="For Join A Channel." , inline=False)
        embed.add_field(name="shuffle" , value="For Empty Queue." , inline=False)
        embed.add_field(name="Error You Will Have" , value=f"\n→If play a songs didn't join and play/no sound/didn't send embed please simply do `=leave`."  f"\n→Bot Will Be Leave In Two Hours If Nothing Have Been Play In That Moment." , inline=False)
        embed.set_footer(text="This Bot Is Program By Python" , icon_url="https://cdn.discordapp.com/emojis/889708830827626578.png?size=96")
        embed.timestamp=datetime.utcnow()
        
        await ctx.send(embed=embed)

    @commands.command(aliases=["bot"])
    async def botinfo(self , ctx):
            values = psutil.virtual_memory()
            val2 = values.available * 0.001
            val3 = val2 * 0.001
            val4 = val3 * 0.001

            values2 = psutil.virtual_memory()
            value21 = values2.total
            values22 = value21 * 0.001
            values23 = values22 * 0.001
            values24 = values23 * 0.001

            embedve = discord.Embed(
                title="Bot Info", description="current have nothing", color=discord.Color.blurple())
            embedve.add_field(
                name="Bot Latency", value=f"Bot latency - {round(self.bot.latency * 1000)}ms", inline=False)
            embedve.add_field(name='Hosting Stats', value=f'Cpu usage- {psutil.cpu_percent(1)}%'
                            f'\n'

                            f'\nNumber Of Cores - {psutil.cpu_count()} '
                            f'\nNumber of Physical Cores- {psutil.cpu_count(logical=False)}'
                            f'\n'

                            f'\nTotal ram- {round(values24, 2)} GB'
                            f'\nAvailable Ram - {round(val4, 2)} GB')
            await ctx.send(embed=embedve)

    @cog_ext.cog_slash(name="botinfo")
    async def botinfo(self , ctx):
            values = psutil.virtual_memory()
            val2 = values.available * 0.001
            val3 = val2 * 0.001
            val4 = val3 * 0.001

            values2 = psutil.virtual_memory()
            value21 = values2.total
            values22 = value21 * 0.001
            values23 = values22 * 0.001
            values24 = values23 * 0.001

            embedve = discord.Embed(
                title="Bot Info", description="current have nothing", color=discord.Color.blurple())
            embedve.add_field(
                name="Bot Latency", value=f"Bot latency - {round(self.bot.latency * 1000)}ms", inline=False)
            embedve.add_field(name='Hosting Stats', value=f'Cpu usage- {psutil.cpu_percent(1)}%'
                            f'\n'

                            f'\nNumber Of Cores - {psutil.cpu_count()} '
                            f'\nNumber of Physical Cores- {psutil.cpu_count(logical=False)}'
                            f'\n'

                            f'\nTotal ram- {round(values24, 2)} GB'
                            f'\nAvailable Ram - {round(val4, 2)} GB')
            await ctx.send(embed=embedve)

    @commands.command(name="ping")
    async def ping(self , ctx):
        my_embed=(discord.Embed(title=":ping_pong: **Pong!**" , 
            description=f"Current latency **{round(self.bot.latency * 1000 , 1)}ms** " , 
            color=discord.Color.blurple())

    )
        await ctx.send(embed=my_embed)

    @cog_ext.cog_slash(name="ping" , description="For Fun")
    async def ping(self , ctx):
        my_embed=(discord.Embed(title=":ping_pong: **Pong!**" , 
            description=f"Current latency **{round(self.bot.latency * 1000 , 1)}ms** " , 
            color=discord.Color.blurple())

    )
        await ctx.send(embed=my_embed)

def setup(bot):
    bot.add_cog(Info_cog(bot))