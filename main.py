import discord
from discord.ext import commands

client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("ready")

@client.command()
async def moin(ctx):
    await ctx.send("Hi")

@client.command()
async def Moin(ctx):
    await ctx.send("Hi")

@client.command()
async def Hi(ctx):
    await ctx.send("Moin")

client.run('ODE0ODI3MDU3MzkzNDM0NjU0.YDjg1Q.Hdw1qRWPYGbW8NMXoI9dHRPVIO0')
