#SeBot by r3dm4n

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


SeBot = commands.Bot(command_prefix='-')
application = """
Hello, I am SeHubs discord bot. Here we will complete your application for the server.
Recruitment: General Introduction: We are looking for mature and dedicated SE'rs,
Refunders etc to be part of an upcoming SE based server. 
Every applicant will go through the same trialling process. 
After their application has been considered by multiple members of 
higher ranking Staff. Proof of a successful Refund/SE's will be necessary
for further analysis and reflection of the individual. If accepted,
the applicant will be given the Verified rank and be supervised
by staff members to guarantee no risk of leaching.
"""
@SeBot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + SeBot.user.name)
    print ("With the ID: " + SeBot.user.id)

@SeBot.command(pass_context=True)
async def ping(ctx):
    await SeBot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@SeBot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await SeBot.say("The users name is: {}".format(user.name))
    await SeBot.say("The users ID is: {}".format(user.id))
    await SeBot.say("The users status is: {}".format(user.status))
    await SeBot.say("The users highest role is: {}".format(user.top_role))
    await SeBot.say("The user joined at: {}".format(user.joined_at))

@SeBot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await SeBot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await SeBot.kick(user)

@SeBot.command(pass_context=True)
async def verify(ctx):
    author = ctx.message.author
    await SeBot.say("Your request has been recieved, please check your messages to finish your application.")
    await SeBot.send_message(author, application)


    #channel = SeBot.get_channel('447438408730542081')
    #if message.content == "cookie":
        
    #    await SeBot.send_message(message.channel, content = "Hello!")  
      #await SeBot.say("Cookies")



SeBot.run("NDQ4Mjg2MTMzNTA4NjM2Njg0.DeT6-A.g23JmJFW2iWBz-XVaKZHPxakFlo")

