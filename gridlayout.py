from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGridLayoutApp(App):
    def build(self):
        layout = GridLayout(cols=2,row_force_default=True,row_default_height=200)
        btn1 = Button(text="Button 1")
        btn2 = Button(text="Button 2")
        btn3 = Button(text="Button 3")
        btn4 = Button(text="Button 4")
        btn5 = Button(text="Button 5")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        return layout
    
MyGridLayoutApp().run()