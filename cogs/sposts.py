"""This module has the implementations for useless commands."""

import discord
from discord.ext import commands

import random
import typing # For optional parameters.


class Sposts(commands.Cog):
    def __init__(self, client):
        self._client = client
        self._random_responses = (
            "travis smells like he didn't make it to the toilet",
            ":yawning_face:", "please please stfu", "100 gecs is ass",
            "you're looking kinda cute today",
            "gimme head",
            "your breath smells like shit :sick:",
            "https://tenor.com/view/love-slobber-gay-black-tongue-gif-15324315",
            "dont @ me, only some people know what's wrong",
            "god your feet are tiny", "your arms look like cigarettes",
            "please make out with me", "who tf is Ellis Rivera?",
            "okay maybe it happened. But 6 million?", 
            "the person who @'d me is a redditor!",
            "https://media.discordapp.net/attachments/759192495782625292/791922820484956210/image0-3.gif"
        )
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.name == "OppositeDay" and len(message.content) > 600:
            await message.channel.send("Too long, not gonna read. :yawning_face:")
        elif message.author.name == "Vsaucey" and message.raw_mentions == [788977882261225483]:
            # Get the message author's ID and fetch the member object.
            author_id = message.author.id
            member_obj = await message.guild.fetch_member(author_id)
            # Mention them 5 times.
            for _ in range(5):
                await message.channel.send(f"{member_obj.mention} yo Travis")
        elif message.author.name == "lazy" and message.raw_mentions == [788977882261225483]:
            author_id = message.author.id
            member_obj = await message.guild.fetch_member(author_id)

            await message.channel.send(f"{member_obj.mention} brap")
        elif message.raw_mentions == [788977882261225483]:
            if random.random() < 0.95:
                await message.channel.send(random.choice(self._random_responses))
            else:
                await message.channel.send("You")
                await message.channel.send("are")
                await message.channel.send("so")
                await message.channel.send("fucking")
                await message.channel.send("hot")


        # await self._client.process_commands(message)
    
    @commands.command()
    async def fill_garbage(self, ctx, amount=5):
        for _ in range(amount):
            # Choose a random message length between 5 and 200 characters.
            rMsgLen = random.randint(5, 200)
            output = ""     # The output string.
            for _ in range(rMsgLen):
                output += random.choice("abcdefghijklmnopqrstuvwxyz ")
            
            # Send the message.
            await ctx.send(output)
    
    @commands.command()
    async def downvote(self, ctx, amount: typing.Optional[int]=5):
        """Downvote the most recent AMOUNT messages."""
        async for message in ctx.channel.history(limit=amount):
            await message.add_reaction("👎🏿")
    
    @commands.command()
    async def upvote(self, ctx, amount=5):
        """Upvote the most recent AMOUNT messages."""
        async for message in ctx.channel.history(limit=amount):
            await message.add_reaction("<:redditupvote:736340551124910090>")
    
    @commands.command()
    async def travis(self, ctx, amount=5):
        travis_emojis = ["🇹", "🇷", "🅰️", "🇻", "🇮", "🇸"]
        async for message in ctx.channel.history(limit=amount):
            for emoji in travis_emojis:
                await message.add_reaction(emoji)

    @commands.command()
    async def react(self, ctx, amount: typing.Optional[int]=5, *emojis):
        """React to the most recent AMOUNT messages with emojis."""
        async for message in ctx.channel.history(limit=amount + 1):
            if message != ctx.message:
                for emoji in emojis:
                    await message.add_reaction(f"{emoji}")
    
    @commands.command()
    async def clear_reactions(self, ctx, amount=5):
        async for message in ctx.channel.history(limit=amount):
            await message.clear_reactions()
    
        

def setup(client):
    client.add_cog(Sposts(client))
