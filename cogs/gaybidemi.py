import json
from discord.ext import commands
import discord

class GayBiDemi(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = json.load(open('data/gaybidemi.json'))
    
    @commands.Cog.listener()
    async def on_message(self, message):
        # Don't check bots, don't check DMs and don't check outside of The Gay, The Bi and The Demi
        if message.author.bot or isinstance(message.channel, discord.DMChannel) or message.guild.id != 690034144289226854:
            return
        
        for word in message.content.split(' '):
            if word.lower() in self.config['filter']:
                try:
                    await message.delete()
                    await message.author.send(f'Please refrain from saying "{word}" in our server, thanks! :D')
                    self.bot.logging.info(f'{message.author.name} tried to say {word}.')
                except:
                    await message.author.send(f'Please refrain from saying "{word}" in our server, thanks! :D"')

def setup(bot):
    bot.add_cog(GayBiDemi(bot))
    bot.logging.info("The Gay, The Bi and The Demi cog was loaded.")