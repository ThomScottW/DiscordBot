### Python script that implements the discord bot named Hubert.

import discord
from discord.ext import commands

import os # For loading cogs (extensions).


# Create an Intents that allows the priveleged intent of viewing data about
# the members of a guild.
intents = discord.Intents.default()
intents.members = True
# Create a "client" (bot), with the prefix "."
client = commands.Bot(command_prefix = ".", intents=intents)


@client.event
async def on_ready():
    """The bot is ready to execute commands."""
    print("Hubert is online.")


@client.command()
async def load(ctx, extension):
    """Load a given extension.
    
    Usage: "load <extension>"
    """
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    """Unload a given extension.
    
    Usage: "unload <extension>"
    """
    client.unload_extension(f"cogs.{extension}")


@client.command()
async def reload(ctx, extension):
    """Reload a given extension.

    Usage: "reload <extension>"
    """
    # Delete the command that invoked this.
    await ctx.message.delete()

    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


# Load all available extensions.
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


# Run the client, using the discord API key.
client.run("")
