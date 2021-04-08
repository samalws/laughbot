import discord
from discord.ext import commands


tk = open('token','r')
DISCORD_TOKEN = tk.read().replace('\n','').replace('\r','')
tk.close()

client = discord.Client()
bot = commands.Bot(command_prefix='>')

ffmpeg_options = {
    'options': '-vn'
}


@bot.command(name='join', help='joins voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='dc', help='leaves voice channel')
async def dc(ctx):
  server = ctx.message.guild.voice_client
  await server.disconnect()


@bot.command(name='laugh', aliases=['lol','lmao'], help='plays laugh track')
async def laugh(ctx, filename='laugh'):
  if not filename.isalnum():
    ctx.send("fuck off.")
    return
  
  filename += ".mp3"
  print(filename)
  try:
    server = ctx.message.guild
    voice_channel = server.voice_client

    if(voice_channel is None):
      await join(ctx)
      voice_channel = server.voice_client

    audio_source = discord.FFmpegPCMAudio(filename)
    voice_channel.play(audio_source)
    
    

  except:
    await ctx.send("fuck off. ")


print("started")
bot.run(DISCORD_TOKEN)
