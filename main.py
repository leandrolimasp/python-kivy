from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.popup import Popup 


Builder.load_file('main.kv')

class Menu(Screen):
    def sair(self):
        Sair().open()

class Sair(Popup):
    pass

class Carrinho(Screen):
    pass

class Consulta(Screen):
    pass

class Menu2(Screen):
    pass

class Widgets(ScreenManager):
    def __init__(self):
        super().__init__()
        self.add_widget(Menu(name='menu'))
        self.add_widget(Carrinho(name='carrinho'))
        self.add_widget(Consulta(name='consulta'))
        self.add_widget(Menu2(name='menu2'))

class TabloideApp(App):
    def build(self):
        return Widgets()

TabloideApp().run()