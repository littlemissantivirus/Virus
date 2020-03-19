from discord.ext import commands
import discord

class Oss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='oss', alias='github', description='Sends a link to my GitHub repo!')
    async def oss(self, ctx):
        await ctx.send(f"My code can be found at https://github.com/littlemissantivirus/Virus")

def setup(bot):
    bot.add_cog(Oss(bot))
    bot.logging.info(f"The command oss was loaded!")