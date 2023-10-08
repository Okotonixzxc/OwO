import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    def throw(self):
        number = random.randint(1,2)
        if number == 1:
            self.monetka.text = 'Орел!'
        if number == 2:
            self.monetka.text = 'Решка!'
    def pred(self):
        self.predict.text = random.choice(['ДА', 'Нет'])

class RandomApp(App):
    def build(self):
        return MyRoot()

randomApp = RandomApp()
randomApp.run()