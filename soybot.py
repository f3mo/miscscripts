import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(file=discord.File('face.jpeg'), delete_after=2.0)
    if 'soy' in message.content:
        await message.channel.send('Soyjack')





client.run('ODM0ODg2MjE3MTcwMTU3NjY5.YIHaYQ.zR7z0CmZ0sBLKipsWl-9E5VvMxI')


