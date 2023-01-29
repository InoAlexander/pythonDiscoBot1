import os
import youtube_dl
import asyncio

voice_client = {}
    
yt_dl_opts = {'format': 'bsestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
    
ffmpeg_options = {'options': "-vn"}