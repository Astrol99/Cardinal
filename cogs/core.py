import discord
from discord.ext import commands

class Core:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Core(bot))