
import string
import random
import discord

print("Made by idex")
print("Contact me for more source codes")
client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}' . format(client))
 
 
Key_Len = 24
 
 
Link = 'https://discord.gift/'
 
Generator = (string.ascii_letters + string.digits)#This is generator's base
Generator1 = [random.choice(Generator)for i in range(Key_Len)]
Generator2 = (''.join(Generator1))
  
print(Generator2)
 
@client.event
async def on_message(message):
   if message.content.startswith('$nitro'): 
     await message.channel.send(Link + Generator2)
     await message.channel.send(Link + Generator2)
     await message.channel.send(Link + Generator2)
     await message.channel.send(Link + Generator2)
     await message.channel.send(Link + Generator2)
     await message.channel.send(Link + Generator2)
     await message.channel.send(Link + Generator2)
        
client.run('Bot_Token_Here')
# Bot by Dhruv Jadav#1620
