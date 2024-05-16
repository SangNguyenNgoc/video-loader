import os

import discord
from discord.ext import commands

CHANNEL_ID = 1238716695636475904

bot = discord.Client(intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


async def upload(path):
    # await bot.start(BOT_TOKEN)
    # Giả sử bạn muốn tải video vào thư mục hiện tại
    channel = bot.get_channel(CHANNEL_ID)
    message = await channel.send(file=discord.File(path))
    # Xóa file sau khi tải lên nếu không muốn giữ lại
    video_link = message.attachments[0]
    print(video_link)
    os.remove(path)
    # await bot.close()
    return video_link


# bot.run(BOT_TOKEN)