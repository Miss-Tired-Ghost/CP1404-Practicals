"""
Simple one way converter.
Code By: April First/Miss Ghost
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.60934


class ConvertMilesKmApp(App):
    """Define App functionality"""
    output_kilometers = StringProperty()

    def build(self):
        """Initialise Kivy App instance"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_kilometers = ''
        return self.root

    def convert_miles_km(self):
        """Convert miles to kilometers, uses the get_miles helper function"""
        kilometers = KM_PER_MILE * self.get_miles()
        self.output_kilometers = str(kilometers)

    def handle_increment(self, increment):
        """Increment/Decrement miles by 1, uses the get_miles helper function"""
        miles = self.get_miles() + increment
        self.root.ids.input_miles.text = str(miles)

    def get_miles(self):
        """Get miles as float from text input object, invalid input results in 0.0"""
        text = self.root.ids.input_miles.text
        try:
            miles = float(text)
        except ValueError:
            miles = 0.0
        return miles


ConvertMilesKmApp().run()
