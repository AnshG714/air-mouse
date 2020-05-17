from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Line
from kivy.clock import Clock
import serial


class DrawInput(Widget):
    def __init__(self, **kwargs):
        super(DrawInput, self).__init__(**kwargs)
        self.b = Button(
            text="clear",
            pos=(1450, 1050))

        self.b.bind(on_press=self.clear)

        self.add_widget(self.b)

        refresh_time = 5
        Clock.schedule_interval(self.timer, refresh_time)

    def timer(self, dt):

        # just a placeholder to test timed serial stuff.
        self.canvas.clear()
        self.remove_widget(self.b)
        self.add_widget(self.b)

        # actual implementation, ask Apu how he's sending data
        value = frdm.readline()

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
            super(DrawInput, self).on_touch_down(touch)
            self.remove_widget(self.b)
            self.add_widget(self.b)

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        pass

    def clear(self, instance):
        self.canvas.clear()


class SimpleKivy4(App):

    def build(self):
        return DrawInput()


if __name__ == "__main__":

    try:
        frdm = serial.Serial('/dev/tty.usbmodem1421', 9600)  # replace

    except:
        print("failed to connect")
        exit()

    SimpleKivy4().run()

    frdm.close()
