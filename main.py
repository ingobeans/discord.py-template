import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

TOKEN = "discord bot token"


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("with beans"))

@client.command()
async def cmd(ctx):
    await ctx.send("This is a command 🤠, " + ctx.author.name)

@client.event
async def on_message(message):
    if message.content == "msg":
        await message.channel.send("Normal message, " + message.author.name)
    
    #if you use commands along with on_message, this line is required for the commands to work.
    await client.process_commands(message)

client.run(TOKEN)