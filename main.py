import discord
from discord.ext import commands
import os
import random

# Configuración del bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

# Saludo de bienvenida
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(123456789012345678)  # Reemplaza con el ID de tu canal
    if channel:
        await channel.send(f'🎉 Bienvenido al servidor {member.mention} !')
    await member.send('¡Hola! Bienvenido al servidor.')

# Comando de motivación
@bot.command()
async def motivacion(ctx):
    frases = [
        "¡Sigue adelante, lo estás haciendo genial! 😃",
        "No te rindas, cada día es una nueva oportunidad. 💪",
        "Cree en ti mismo y en tus habilidades. 😉",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día. ✨",
        "Un mal día no significa una mala vida. ¡Ánimo! 🌈"
    ]
    await ctx.send(random.choice(frases))

# Comando cuando alguien esté triste
@bot.command()
async def triste(ctx):
    await ctx.send("😢 Lo siento mucho. Si necesitas hablar, aquí estoy para escucharte.")

# Comando ping (responde rápido con la latencia del bot)
@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def guarda_imagen(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo = archivo.filename
        url_archivo = archivo.url
        await archivo.save(f'./{nombre_archivo}')
        await ctx.send(f'Imagen guardada como {nombre_archivo}')
    else:
        await ctx.send('Por favor, adjunta una imagen para guardar.')

        #bot command que reciba imagen, la guarde y use la funcion get_class de model.py
from model import get_class  # Importar la función desde model.py
@bot.command()
async def clasifica(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo = archivo.filename
            url_archivo = archivo.url
            await archivo.save(f'./{nombre_archivo}')
            await ctx.send(f'Imagen guardada como {nombre_archivo}')

            model_path = 'keras_model.h5'  # Ruta al modelo
            labels_path = 'labels.txt'     # Ruta a las etiquetas
            image_path = f'./{nombre_archivo}'  # Ruta a la imagen guardada

            class_name, confidence_score = get_class(model_path, labels_path, image_path)
            await ctx.send(f'La imagen se clasificó como {class_name}, con una confianza de {confidence_score:.2f}')
    else:
        await ctx.send('No hay imagen para clasificar.')

bot.run('TU_TOKEN_A')




