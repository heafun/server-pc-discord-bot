from discord import Message, Client
import sys
import inspect
import models.commands as commands
from models.commands import Command


class MessageHandler:
    def __init__(self, client: Client = None):
        self.client = client
        self.commands = []

        for name, obj in inspect.getmembers(sys.modules[commands.__name__], inspect.isclass):
            if issubclass(obj, Command) and name != Command.__name__:
                self.commands.append(obj)

    def set_client(self, client):
        self.client = client

    async def handle_message(self, message: Message):
        if message.content[0] != '!':
            return

        if message.author == self.client.user:
            return

        for obj in self.commands:
            if obj.__name__.lower() == message.content[1:].lower():
                command: Command = obj()

                await command.run(message)
                return
            else:
                obj.__name__.lower()
