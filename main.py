from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class BoxLayoutExample(BoxLayout):
    pass
#u can add button here or in kv file i can use Label
#instead of using Button
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="c")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""
        
#https://youtu.be/l8Imtec4ReQ?t=1625
class MainWidget(Widget):
    pass
class TheLabApp(App):
    pass

#https://youtu.be/l8Imtec4ReQ?t=1226
TheLabApp().run()