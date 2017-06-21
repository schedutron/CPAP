import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class GridLayoutApp(App):
    def build(self):
        return GridLayout()

glApp = GridLayoutApp()
glApp.run()
