import PySimpleGUI as PGui


class MainGui:
    def __init__(self):
        self.layout = [[PGui.Text("Placeholder Text")]]

    def open(self):
        window = PGui.Window('ServerPc-Bot', self.layout)

        while True:
            event, values = window.read()
            if event in (None, 'Exit'):
                break
            if callable(event):
                event()
