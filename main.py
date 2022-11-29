# Import stuff heh
## discord.py
import discord
## keep_alive.py
import keep_alive
## some other stuff
from mcstatus import MinecraftServer
from decouple import config
from MaxEmbeds import EmbedBuilder

# keep_alive to receive ping.
keep_alive.keep_alive()

# Start server, with commands and stuff.
server = MinecraftServer.lookup(config('ADDRESS'))
skyblock = MinecraftServer.lookup(config('SKYBLOCKADDRESS'))
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Made with <3 by NguyenAnDev :3')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!status'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Oh hey, Soul Survival is online :D",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "SOULSURVIVAL.EU.ORG", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Unfortunately, Soul Survival went offline :(",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)

    if message.content.startswith('!stasus'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Sussy baka, Soul Survival is online :D",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "SOULSURVIVAL.EU.ORG", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Man, so sus, and Soul Survival went offline :(",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops so sus, **Soul Survival** **is currently offline**!')

    if message.content.startswith('!statú'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Telex user huh? Nevermind, Soul Survival is online :D",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "SOULSURVIVAL.EU.ORG", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Telex user huh? Welp, Soul Survival is offline :(",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)

    if message.content.startswith('!stasú'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Sussy baka, Soul Survival is online :D",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "SOULSURVIVAL.EU.ORG", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Man, so sus, and Soul Survival is offline :(",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)

            #await message.channel.send('Unikey user huh? Nevermind, wait... **Soul Survival** **is currently offline**!')

    ## remave ping cuz if i hosted it on the same machine. ping = 0.xx ms => useless
    if message.content.startswith('!players'):
        try:
            player = server.status()
            playerskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Soul Survival Playercount",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["From", "SoulMC With <3", True], ["Survival", "{0}/50".format(playerskyblock.players.online), True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Soul Survival is offline :(",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Soul Survival** is currently **offline**!')

    if message.content.startswith('!playẻ'):
        try:
            player = server.status()
            playerskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Telex user? Anyways here is the Soul Survival Playercount",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["From", "SoulMC With <3", True], ["Survival", "{0}/50".format(playerskyblock.players.online), True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Telex user? Nevermind, Soul Survival is offline :(",
                description="Powered by SoulStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Soul Survival** is currently **offline**!')

    ## remave ping cuz if i hosted it on the same machine. ping = 0.xx ms => useless (from typical)
    # ping is still here as i also want to get the ping from my webserver when the mainserver is off (in the near future)

    if message.content.startswith('!ping'):
        try:
            latency = server.ping()
            latencyskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Soul Survival Latency from Replit",
                description="Powered by SoulStatus, hosted on Replit",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["From Soul", "MC with <3".format(latency), True], ["Survival Latency (ms)", "{0} from Replit.".format(latency), True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Soul Survival is offline and I can't check the latency :(",
                description="Powered by SoulStatus, hosted on Replit",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Soul Survival** is currently **offline**!')

    if message.content.startswith('!latency'):
        try:
            latency = server.ping()
            latencyskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Soul Survival Latency from Replit",
                description="Powered by SoulStatus, hosted on Replit",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["From SoulMC", "with <3".format(latency), True], ["Survival Latency (ms)", "{0} from Replit.".format(latency), True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Soul Survival is offline and I can't check the latency :(",
                description="Powered by SoulStatus, hosted on Replit",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":cry:", True]],
                thumbnail='https://media.discordapp.net/attachments/1014729522718973953/1046809885746151495/standard.gif'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Soul Survival** is currently **offline**!')

client.run(config('TOKEN'))
