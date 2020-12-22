import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER_NAME')

client = discord.Client()


class ScriptedResponse:

    def __init__(self, triggers, response):
        self.triggers = triggers
        self.response = response

    def triggered(self, message):
        if isinstance(message, str):
            msg_lower = message.lower()
        elif isinstance(message, discord.Message):
            msg_lower = message.content.lower()
        else:
            raise TypeError(f"Unsupported message type {type(message)}")
        
        for t_ in self.triggers:
            if t_ in msg_lower:
                return True
        return False


zoidberg = ScriptedResponse(
    ['who can', 'who will', 'why not'],
    "Why not zoidberg? <:zoidberg:790395677305470977>"
)

professor_farnsworth = ScriptedResponse(
    ['good news', "that's good"],
    "https://tenor.com/view/futurama-good-news-good-professor-gif-13624955"
)

fry = ScriptedResponse(
    ['good deal', 'very nice', 'shut up and take my money', 'i want it', 'i want that',
     'i love it', 'i like it'],
    "https://tenor.com/view/money-dollars-cash-rich-shut-up-and-take-my-money-gif-3555042"
)


futurama_characters = [
    professor_farnsworth,
    zoidberg,
    fry,
]
    

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    
    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name} (id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    for character in futurama_characters:
        if character.triggered(message):
            await message.channel.send(character.response)


client.run(TOKEN)

