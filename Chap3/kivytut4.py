import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SampGridLayout(GridLayout):
    pass

class SampleApp(App):
    def build(self):
        return SampGridLayout()
sample_app = SampleApp()
sample_app.run()
