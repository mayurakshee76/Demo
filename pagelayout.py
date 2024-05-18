from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

class MyLayoutApp(App):
    def build(self):
        layout = PageLayout()

        btn1 = Button(text="Hello", size_hint=(None,None), width=100)
        btn2 = Button(text="World", size_hint=(None,None), width=100)

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout
    
MyLayoutApp().run()