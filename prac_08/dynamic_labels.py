"""
Dynamically Creates Labels for each name in list
Code By: April First/Miss Ghost
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Demo Dynamic Widget Creation"""
    def __init__(self, **kwargs):
        """Initialise main app instance"""
        super().__init__(**kwargs)
        self.NAMES = ["Alessia Herring",
                      "Henrik Gross",
                      "Angel Wright",
                      "Grayson May",
                      "Adriana Willis",
                      "Remington Arroyo",
                      "Kyra Martin",
                      "Mateo Montgomery",
                      "Evangeline Randall",
                      "Trenton Boyer"]

    def build(self):
        """Build Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels from list of names"""
        for name in self.NAMES:
            temp_label = Label(text=name)
            temp_label.text_color = (1, 0, 0, 1)
            temp_label.background_color = (1, 1, 1, 1)

            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
