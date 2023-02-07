import discord
import _thread as thread


class DiscordClient:
    def __init__(self, message_handler, token):
        self.token = token

        self.message_handler = message_handler

        intents = discord.Intents.all()
        self.client = discord.Client(intents=intents)

        self.message_handler.set_client(self.client)

        @self.client.event
        async def on_ready():
            print(f'Logged in as {self.client.user}')

        @self.client.event
        async def on_message(message):
            await self.message_handler.handle_message(message)

    def start(self):
        thread.start_new_thread(self.client.run, (self.token,))
