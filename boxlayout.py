#For adding more the one items
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor=(1,0,1,1)
Window.size=(330,550)


class MyButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=10,padding=10)

        btn1 = Button(text="Button 1")
        btn2 = Button(text="Button 2")
        btn3 = Button(text="Button 3")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

MyButtonApp().run()