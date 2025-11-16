import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    # Prevent the bot from replying to itself
    if message.author == self.user:
        return

    # Respond to a message starting with "$hello"
    if message.content.startswith('$meme'):
        await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQzMzAzMjE4NjAxNzIxODU3MA.G7BSjp.VB5N927ARwyWpu7svyvYb8RBv7XrtetK-DElVA') # Replace with your own token.