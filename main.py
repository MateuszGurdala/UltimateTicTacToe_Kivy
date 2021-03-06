from kivy.config import Config

Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 800)
Config.set('graphics', 'top', 50)
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'borderless', 'true')

from imports import *
from main_app import GameManager

val = 50
Window.size = 9 * val, 19.5 * val


class MainApp(App):
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.title = "UltimateTicTacToe"
        self.colors = colors

    @staticmethod
    def build():
        return GameManager()


if __name__ == "__main__":
    MainApp().run()
