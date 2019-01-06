# -*- coding: utf-8 -*
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')
import kivy
kivy.require('1.10.1')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.utils import get_color_from_hex
from kivy.resources import resource_add_path

from kivy.factory import Factory

# デフォルトに使用するフォントを変更する
resource_add_path('fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class StartScreen(BoxLayout):
    pass

class TestRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(TestRoot, self).__init__(**kwargs)

    def go_checkScreen(self):   
        self.clear_widgets()
        checkscreen = Factory.checkscreen()
        self.add_widget(checkscreen)

class TestApp(App): 
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '映画レコメンドシステム'

if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    TestApp().run()