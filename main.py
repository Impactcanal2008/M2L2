import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('¬hola'):
        await message.channel.send("Hola!")
    elif message.content.startswith('¬adiós'):
        await message.channel.send("Adiós!")
    elif message.content.startswith('¬qué es el cambio climático?'):
        await message.channel.send("Es un proceso que el ser humano ha creado y hace que el mundo se caliente")
    elif message.content.startswith('¬por qué hay que detener el cambio climático?'):
        await message.channel.send("Para que la vida en la Tierra siga siendo diversa y no se extingan más especies")
    elif message.content.startswith('¬qué puedo hacer para evitar el cambio climático?'):
        await message.channel.send("""Hay muchas cosas que puedes hacer para reducir los efectos del cambio climático:
                                   -Utilizar menos papel
                                   -Utilizar bolsas reutilizables
                                   -Ir a manifestaciones para que el gobierno y las empresas reduzcan su consumo
                                   -No tirar las cosas al suelo o al mar
                                   -Conciencia a tu entorno para que el mundo sea un lugar mejor""")
    elif message.content.startswith('¬cuánto daño ha hecho el cambio climático?'):
        await message.channel.send("De momento, ha hecho que la temperatura aumente 1.5ºC a nivel global. Además, está poniendo en peligro a muchas especies, como los osos panda y los pingüinos")
    elif message.content.startswith('¬adiós'):
        await message.channel.send("Adiós!")
client.run("MTE1ODA1NTY4OTAwOTI1NDU0MA.GWtOIZ.6UbqZXH-PtJ_z4oDmeNtb7BBp5foDcLfyW4VgI")