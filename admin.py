import discord
import asyncio

from discord.ext import commands
from discord_slash import cog_ext , SlashContext

class Admin_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin_cog Loaded Succesfully.')

    @commands.command(description="Unmutes a specified user.")
    async def unmute(self , ctx, member: discord.Member=None):
        if not member:
            await ctx.send("You must mention a member to unmute!")

        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await member.send(f" you have unmuted from: - {ctx.guild.name}")
        embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.blurple())
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(description="Unmutes a specified user.")
    async def unmute(self , ctx, member: discord.Member=None):
        if not member:
            await ctx.send("You must mention a member to unmute!")
            
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await member.send(f" you have unmuted from: - {ctx.guild.name}")
        embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.blurple())
        await ctx.send(embed=embed)

    @commands.command()
    async def mute(self , ctx, member: discord.Member=None, time=None, *, reason=None):
        if not member:
            await ctx.send("You must mention a member, time and reason(or no) to mute!")
        elif not time:
            await ctx.send("You must mention a time!")
        else:
            if not reason:
                reason="No reason given"
            try:
                seconds = int(time[:-1]) 
                duration = time[-1] 
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    await ctx.send("Invalid duration input")
                    return
            except Exception as e:
                print(e)
                await ctx.send("Invalid time input")
                return
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name="Muted")
            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            await member.add_roles(mutedRole, reason=reason)

            muted_embed = discord.Embed(title="Muted", description=f"{member.mention} Was muted" , color=discord.Color.blurple())
            muted_embed.add_field(name="Reason:" , value=reason)
            muted_embed.add_field(name="Duration:" , value=time)
            await ctx.send(embed=muted_embed)
            await member.send(f"You Have Been Muted From: {guild.name} reason: {reason} time: {time}")
            await member.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")
            await asyncio.sleep(seconds)

            await member.remove_roles(mutedRole)
            
            unmute_embed = discord.Embed(title="Mute Over", description=f"{member.mention} muted is over" , color=discord.Color.blurple())
            await ctx.send(embed=unmute_embed)


    @cog_ext.cog_slash(description="For Mute A Member")
    async def mute(self , ctx, member: discord.Member=None, time=None, *, reason=None):
        if not member:
            await ctx.send("You must mention a member, time and reason(or no) to mute!")
        elif not time:
            await ctx.send("You must mention a time!")
        else:
            if not reason:
                reason="No reason given"
            try:
                seconds = int(time[:-1]) 
                duration = time[-1] 
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    await ctx.send("Invalid duration input")
                    return
            except Exception as e:
                print(e)
                await ctx.send("Invalid time input")
                return
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name="Muted")
            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            await member.add_roles(mutedRole, reason=reason)

            muted_embed = discord.Embed(title="Muted", description=f"{member.mention} Was muted" , color=discord.Color.blurple())
            muted_embed.add_field(name="Reason:" , value=reason)
            muted_embed.add_field(name="Duration:" , value=time)
            await ctx.send(embed=muted_embed)
            await member.send(f"You Have Been Muted From: {guild.name} reason: {reason} time: {time}")
            await member.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")
            await asyncio.sleep(seconds)

            await member.remove_roles(mutedRole)
            
            unmute_embed = discord.Embed(title="Mute Over", description=f"{member.mention} muted is over" , color=discord.Color.blurple())
            await ctx.send(embed=unmute_embed)

    ##################################################

    @commands.command(name="warn")
    async def warn(self , ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="You have been warn" , description=f"{member.mention} was warned " , color=discord.Color.blurple())
        embed.add_field(name="reason:" , value=reason , inline=False)
        await ctx.send(embed=embed)
        await ctx.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")
        await member.send(f"You have been warn reason: {reason}")
        await member.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")

    @cog_ext.cog_slash(name="warn")
    async def warn(self , ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="You have been warn" , description=f"{member.mention} was warned " , color=discord.Color.blurple())
        embed.add_field(name="reason:" , value=reason , inline=False)
        await ctx.send(embed=embed)
        await ctx.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")
        await member.send(f"You have been warn reason: {reason}")
        await member.send("https://cdn.discordapp.com/attachments/880086279021297664/915230250978394122/ba29496e40b03d78.jpg")

def setup(bot):
    bot.add_cog(Admin_cog(bot))