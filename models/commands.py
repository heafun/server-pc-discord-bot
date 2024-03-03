import inspect
import sys
from discord import Message
import urllib.request

from models.permission import Permission


class Command:
    async def run(self, message):
        pass

    def get_permissions(self) -> Permission:
        pass

    def get_description(self) -> str:
        pass


class ServerIp(Command):
    async def run(self, message: Message):
        ip = urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')
        await message.channel.send(ip)

    def get_permissions(self) -> Permission:
        return Permission()
    
    def get_description(self) -> str:
        return "Gibt die Ip des Servers zurück."
    

class Help(Command):
    async def run(self, message: Message):
        commands = []

        for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
            if issubclass(obj, Command) and name != Command.__name__:
                commands.append(obj)

        resultText = ""

        for command in commands:
            commandObject = command().get_description()
            resultText += "!" + command.__name__ + " -> " + command().get_description() + "\n"

        await message.channel.send(resultText)

    def get_permissions(self) -> Permission:
        return Permission()
    
    def get_description(self) -> str:
        return "Gibt alle Commands mit Beschreibung zurück, welche du ausführen darfst."
    