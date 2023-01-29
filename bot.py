import discord
import responses 
import os 
import asyncio
import youtube_dl
from youtube_search import YoutubeSearch

intents = discord.Intents.all()


async def send_message (message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA2MTQ2NTIwNzUzODQ2NjkwOA.Gg25Ho.3qKMFPx260poaAjrY_wSkdBt27fJJ7mvT-hUdk'
    client = discord.Client(intents=intents)
    
    
    
    @client.event
    async def on_ready():
        print(f'{client.user} uwu im running senpai O_O')
        print(f"---------------------------------------")
        
    @client.event
    async def on_message(msg):
        if msg.author != client.user:
            if msg.content.lower().startswith("!hi"):
                await msg.channel.send(f"uwu haiii there {msg.author.display_name} senpai!!! =^.^=")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message[0] == '?':
            user_message = user_message[1: ]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)   
        

# --------- moderation ---------
# doesnt work right...

    bad_words = ["hoe", "http://", "nigger", "sand nigger"]
    @client.event
    async def on_message(msg):
        if msg.author != client.user:
            for text in bad_words:
                if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
                    await msg.delete()
                return
        print("not deleting")
        
        
# ---- youtube for music --------\

    # voice_clients = {}
    
    # yt_dl_opts = { 
    #     'format': 'bestaudio/best',
    #     'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    #     'restrictfilenames': True,
    #     'noplaylist': True,
    #     'nocheckcertificate': True,
    #     'ignoreerrors': False,
    #     'logtostderr': False,
    #     'quiet': True,
    #     'no_warnings': True,
    #     'default_search': 'auto',
    #     'source_address': '0.0.0.0'
    #     }
    # ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
    
    # ffmpeg_options = {'options': "-vn",
    #                     "before_options" : "-reconnect1 -reconnect_streamed 1 - reconnect_delay_max 5"
    #                 }
    
    
    # @client.event
    # async def on_message(message):
    #     if message.content.startswith("#play"):
    #         try: 
    #             url = message.content.split()[1]  
    #             voice_client = await message.author.voice.channel.connect()
    #             voice_clients[voice_client.guild.id] = voice_client
                
    #             loop = asyncio.get_event_loop()
    #             data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
                
    #             song = data['url']
    #             player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C:\\ffmpeg\\ffmpeg.exe")
                    
    #             voice_client.play(player)
                    
    #         except Exception as err:
    #             print(err)
        
    async def joinMusicChannel(ctx):
        try:
            channel = ctx.author.voice.channel
        except:
            await ctx.send(ctx.author.mention + " Please join the music voice channel.")
            return False

        vc = ctx.voice_client
        if vc == None:
            await channel.connect()
        return True

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    def endSong(guild, path):
        os.remove(path)


    @client.command()
    async def play(ctx, url):
        data = await joinMusicChannel(ctx)
        if data == True:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                file = ydl.extract_info(url, download=True)
            guild = ctx.message.guild
            voice_client = guild.voice_client
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")

            voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
            voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

        
    client.run(TOKEN)   