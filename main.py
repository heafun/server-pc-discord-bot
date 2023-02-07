import os
from pathlib import Path
import PySimpleGUI as PGui

from business.message_handler import MessageHandler
from business.main_gui import MainGui
from business.discord_client import DiscordClient

messageHandler = MessageHandler()

dataDirString = "data"
if not os.path.exists(dataDirString):
    os.mkdir(Path(dataDirString).name)

tokenFileString = dataDirString + "/token.cfg"
if not os.path.exists(tokenFileString):
    open(tokenFileString, "a").close()

file = open(tokenFileString, "r")
fileContent = file.read()
file.close()

token: str
if len(fileContent) == 0:
    layout = [[PGui.Text("Set a Token:")],
              [PGui.Input()],
              [PGui.Button("Save")]]

    window = PGui.Window("No Token", layout)

    event, values = window.read()
    window.close()

    token = values[0]

    file = open(tokenFileString, "w")
    file.write(token)
    file.close()
else:
    token = fileContent


client = DiscordClient(messageHandler, token)
mainGui = MainGui()
client.start()
mainGui.open()
