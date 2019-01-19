try:
    import discord
    from discord.ext import commands
except Exception as e:
    print(f"[!] Failed to import discord!\n{e}")
import time
import sys

# Make sure to remove before pushing
TOKEN = ""

cogs = [
    "cogs.core"
]

admins = [
    354693078495264778
]

def animation():
    series = [
        "| Loading cogs...",
        "/ Loading cogs...",
        "- Loading cogs...",
        "\ Loading cogs..."
    ]
    for i in range(20):
        sys.stdout.write("\r" + series[i%len(series)])
        sys.stdout.flush()
        time.sleep(0.25)
    print("\n")

bot = commands.Bot(command_prefix="|",
                   status=discord.Status.idle,
                   activity=discord.Game(name="Booting up..."))

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Online"))
    print("[>] Bot is online")
    print("[!] Initiating cogs")
    animation()
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"[!] Successfully loaded {cog}")
        except Exception as e:
            print(f"[*] Failed to load {cog}\n      {e}")
    print("[>] Finished cog sequence")
    print("[>] Live feed of bot:\n")

@bot.command()
async def reload(ctx, *, cog):
    if ctx.author.id not in admins:
        return await ctx.send(f"{ctx.author.mention} | You are not authorized to call this command!")
    try:
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await ctx.send(f"{ctx.author.mention} | [!] Successfully reloaded {cog}")
    except Exception as e:
        error = f"```py\n{e}\n``` "
        await ctx.send(f"{ctx.author.mention} | [!] Failed to reload {cog}\n{error}")

bot.run(TOKEN)