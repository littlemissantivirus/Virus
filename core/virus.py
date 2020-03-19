import discord
from discord.ext import commands, tasks
import json
import logging
import datetime
import sys

class Virus(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the time that the bot was started at.
        self.launchtime = datetime.datetime.utcnow()

        # Setup admins, the config and guild configs.
        self.admins = json.load(open('data/admins.json'))
        self.config = json.load(open('config.json'))
        self.guild_configs = {}
        self.verified_guilds = []
        
        # If `dev.txt` exists then the bot will run under dev mode.
        try:
            open('dev.txt', 'r')
            self.dev = True
        except Exception:
            self.dev = False
        
        # Setup logging.
        logging.basicConfig(filename='virus.log', level=logging.INFO)
        self.logging = logging.getLogger("Virus")
        stdout = logging.StreamHandler(sys.stdout)
        stdout.setLevel(logging.INFO)
        self.logging.addHandler(stdout)

        # Load bot modules
        self.load_cogs()
        # Load commands that are in their own separate files.
        self.load_commands()
    
    def load_commands(self):
        commands = ['commands.oss']
        for command in commands:
            try:
                self.load_extension(command)
            except Exception as ex:
                self.logging.warn(f"Couldn't load the extension {extension}! Reason:\n{ex}")

    def load_cogs(self):
        extensions = ['cogs.gaybidemi']
        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as ex:
                self.logging.warn(f"Couldn't load the extension {extension}! Reason:\n{ex}")


