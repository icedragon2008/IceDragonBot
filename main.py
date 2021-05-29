import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith("Привет"):
      await message.channel.send("Привет!")
    if message.content.startswith("привет"):
      await message.channel.send("Привет!")
    if message.content.startswith("привет."):
      await message.channel.send("Привет!")
    if message.content.startswith("Привет."):
      await message.channel.send("Привет!")

    if message.content.startswith("Как дела"):
      await message.channel.send("Хорошо, а у тебя.")
    if message.content.startswith("как дела"):
      await message.channel.send("Хорошо, а у тебя.")
    if message.content.startswith("Как дела?"):
      await message.channel.send("Хорошо, а у тебя.")
    if message.content.startswith("как дела?"):
      await message.channel.send("Хорошо, а у тебя.")

    if message.content.startswith("Хорошо"):
      await message.channel.send("Круто!")
    if message.content.startswith("хорошо"):
      await message.channel.send("Круто!")
    if message.content.startswith("хорошо."):
      await message.channel.send("Круто!")
    if message.content.startswith("Хорошо."):
      await message.channel.send("Круто!")

    if message.content.startswith("Пока."):
      await message.channel.send("Пока!")
    if message.content.startswith("Пока"):
      await message.channel.send("Пока!")
    if message.content.startswith("пока"):
      await message.channel.send("Пока!")
    if message.content.startswith("пока"):
      await message.channel.send("Пока!")

    if message.content.startswith("?"):
      await message.channel.send("Imato kudasai!")

    if message.content.startswith("Книги"):
      await message.channel.send("https://www.litmir.me/")
    if message.content.startswith("Игры"):
      await message.channel.send("https://store.steampowered.com/")
    if message.content.startswith("Интернет"):
      await message.channel.send("https://www.google.ru/")
    if message.content.startswith("Еда"):
      await message.channel.send("https://eda.yandex.ru/moscow?shippingType=delivery&utm_campaign=50744947.%5BEDA%5DDT_BR-goal_RU-MOS-MOW_brand_restype-search_NU&utm_content=&utm_medium=cpc&utm_source=yasearch&utm_term=еда%7Cpid%7C20180320779%7Caid%7C10555769185&yclid=2918396850298715938")


client.run(os.getenv('ТОКЕН'))