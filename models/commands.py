from discord import Message
import urllib.request


class Command:
    async def run(self, message):
        pass

    def get_permissions(self):
        pass


class ServerIp(Command):
    async def run(self, message: Message):
        ip = urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')
        await message.channel.send(ip)

    def get_permissions(self):
        return
    