"""
CP1404/CP5632 Practical IT@JCU
Convert Miles to Kilometer
Hsu Myat Mon Win
Date: 12/11/2023
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KM = 1.60934
DEFAULT_OUTPUT = 0.0


class ConvertMileToKilometerApp(App):
    """ConvertMileToKilometerApp is a Kivy App for converting miles to kilometers."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Mile To Kilometer"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in Miles & press Convert"
        return self.root

    def handle_convert(self, mile):
        """Convert miles to kilometers and show the output."""
        try:
            km = float(mile) * MILE_TO_KM
            self.message = str(km)
        except ValueError:
            self.message = str(DEFAULT_OUTPUT)

    def handle_increment(self, mile, increment):
        """Increase or decrease the mile number by increment."""
        try:
            mile = float(mile) + increment
            self.root.ids.input_number.text = str(mile)
        except ValueError:
            self.root.ids.input_number.text = str(increment)


ConvertMileToKilometerApp().run()
