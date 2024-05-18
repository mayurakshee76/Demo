from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyTextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=10,padding=150)
        
        self.email = TextInput(text="Enter Your Email")
        self.password = TextInput(text="Enter Password")
        self.submit = Button(text="Log In")
        self.submit.bind(on_press=self.submitbtn)  # Corrected method name

        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(self.submit)

        return layout

    def submitbtn(self, instance):  # Corrected method name
     print(f"Your Email = {self.email.text}")
     print(f"Your Password = {self.password.text}")
MyTextInputApp().run()

