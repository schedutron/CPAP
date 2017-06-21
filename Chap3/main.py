import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()
