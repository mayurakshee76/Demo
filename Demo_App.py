import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

class Homescreen(Screen):
    pass

class FirstScreen(Screen):
    def on_enter(self):
        # Specify the path to the folder containing images
        image_folder = r'Kivy/Codes & Data/Images/girls'

        # Get a list of all image files in the folder
        image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        # Clear any existing widgets from the scroll layout
        self.ids.scroll_view.clear_widgets()

        # Create a new layout to hold the images with GridLayout
        image_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)

        # Add Image widgets for each image file to the layout
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image_widget = Image(source=image_path, size_hint_y=None, height=200)
            image_layout.add_widget(image_widget)

        # Set the height of the GridLayout based on the number of images
        image_layout.bind(minimum_height=image_layout.setter('height'))

        # Add the layout with images to the scroll view
        self.ids.scroll_view.add_widget(image_layout)

class SecondScreen(Screen):
    def on_enter(self):
        # Specify the path to the folder containing images
        self.image_folder = r'Kivy\Codes & Data\Images\boys'

        # Get a list of all image files in the folder
        image_files = [f for f in os.listdir(self.image_folder) if os.path.isfile(os.path.join(self.image_folder, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        # Clear any existing widgets from the scroll layout
        self.ids.image_layout.clear_widgets()

        # Create a new layout to hold the images with GridLayout
        image_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)

        # Add Image widgets for each image file to the layout
        self.image_widgets = []
        for image_file in image_files:
            image_path = os.path.join(self.image_folder, image_file)
            image_widget = Image(source=image_path, size_hint_y=None, height=200)
            image_widget.bind(on_release=lambda img: self.select_image(img, image_path))
            image_layout.add_widget(image_widget)
            self.image_widgets.append(image_widget)

        # Set the height of the GridLayout based on the number of images
        image_layout.bind(minimum_height=image_layout.setter('height'))

        # Add the layout with images to the scroll view
        self.ids.image_layout.add_widget(image_layout)

    def select_image(self, image_widget, image_path):
        for widget in self.image_widgets:
            widget.border = (0, 0, 0, 0)  # Reset borders
        image_widget.border = (2, 2, 2, 2)  # Highlight selected image
        self.selected_image_path = image_path  # Store selected image path

    def proceed_to_blank_page(self):
        self.manager.current = 'BlankPage'
        self.manager.get_screen('BlankPage').ids.selected_image_label.text = self.selected_image_path

class BlankPage(Screen):
    pass

class ImageGalleryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SecondScreen(name='SecondScreen'))
        sm.add_widget(BlankPage(name='BlankPage'))
        return sm

class ImageGalleryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SecondScreen(name='SecondScreen'))
        return sm

class BlankPage(Screen):
    pass
class Manager(ScreenManager):
    pass

class ImageGalleryApp(App):
    def build(self):
        bldr = Builder.load_file("kv.kv")
        return bldr
       # layout = FirstScreen()

        ## Specify the path to the folder containing images
        #image_folder = r'Kivy\Codes & Data\Images\girls'

       # # Get a list of all image files in the folder
        #image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png'))]

       # # Create an Image widget for each image file and add it to the layout
        #for image_file in image_files:
          #  image_path = os.path.join(image_folder, image_file)
           # image_widget = Image(source=image_path)
           # layout.add_widget(image_widget)

       # return layout


#if __name__ == '__main__':
ImageGalleryApp().run()