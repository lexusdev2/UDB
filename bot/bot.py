import nextcord
import pymongo

from nextcord.ext import commands

mclient = pymongo.MongoClient("mongodb://localhost:27017/")
client = commands.Bot(
    command_prefix="!",
    help_command=commands.HelpCommand,
    description="UNITY",
    max_messages=500,
    shard_id=95,
)

@client.command(name="CHECK")
async def check(interaction: nextcord.Interaction):
    interaction.response.send_message("YES!")
    

client.login("")