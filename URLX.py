import discord
import os
from discord import channel
from discord.ext import commands
from discord.team import Team
import logging
import requests
import json

from Bot_Data import *

intents=discord.Intents.default()
intents.members=True

client=commands.Bot(command_prefix='X')

@client.event
async def on_ready():

    print("Yes Dragon X!")
    print("--------------")
    print(" ")

    await client.change_presence(activity=discord.Game('X help'))
    channel=client.get_channel(Channel_Token)
    exit_cond=True

    while(exit_cond):
        inp=input().split()
        initial=inp[0].lower()
        com=inp[1].lower()

        if(initial=="x" or initial=="urlx"):

            if(com=="help"):
                print("push <link> \t\t-> it will push the link in the default channel\nshow \t\t\t-> it will show the last 10 links shared in the default channel\nshow <channel id> \t-> it will show the last 10 links shared in the input channel\nquit \t\t\t-> stop the command inputs")
            if(com=="push"):
                await channel.send(inp[2])

            elif(com=="quit"):
                exit_cond=False

            elif(com=="show"):
                channel_input=channel
                c=0
                links=[]
                desc=""
                output=discord.Embed(title= "Last 10 links shared:\n", colour=0x3498db)

                if(len(inp)>2):
                    if(inp[2][0]=='<'):
                        channel_input=client.get_channel(inp[2][1:19])
                    else:
                        channel_input=client.get_channel(inp[2])
            
                async for msg in channel_input.history(limit=100000):
                    link_check=msg.content.split()
                    for i in range(0, len(link_check)):
                        if(link_check[i][0:4]=="http"):
                            links.append(link_check[i])
                            c+=1
                    if (c==10):
                        break

                for i in range(0, len(links)):
                    desc+=str(i+1)+". "+links[i]+"\n"
                output=discord.Embed(title= "Last 10 links shared:\n", description= desc, colour=discord.Colour.dark_gold())
                
                await channel.send(embed=output)

                
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        inp2=message.content.split()
        initial2=inp2[0].lower()
        com2=inp2[1].lower()
        if(initial2=="x" or initial2=="urlx"):
            if(com2=="help"):
                await message.channel.send("All of my main commands are avaialble through terminal only\nHere only this command is available\nshow \t\t-> it will show the last 10 links shared in this channel\nshow <channel id> \t-> it will show the last 10 links shared in the input channel")
            elif(com2=="show"):
                if(len(inp2)>2):
                    if(inp2[2][0]=='<'):
                        channel_input2=client.get_channel(inp2[2][1:19])
                    else:
                        channel_input2=client.get_channel(inp2[2])
                        
                else:
                    channel_input2=message.channel

                c2=0
                links2=[]
                desc2=""
                output2=discord.Embed(title= "Last 10 links shared:\n", colour=0x3498db)

                async for msg in channel_input2.history(limit=100000):
                    link_check2=msg.content.split()
                    for i in range(0, len(link_check2)):
                        if(link_check2[i][0:4]=="http"):
                            links2.append(link_check2[i])
                            c2+=1
                    if (c2==10):
                        break

                for i in range(0, len(links2)):
                    desc2+=str(i+1)+". "+links2[i]+"\n"
                output=discord.Embed(title= "Last 10 links shared:\n", description= desc2, colour=discord.Colour.dark_gold())
                
                await channel_input2.send(embed=output)
                



client.run(Bot_Token)