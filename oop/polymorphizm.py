import abc


class UIControl(abc.ABC):
    def enable(self):
        print("Enable")

    @abc.abstractmethod
    def draw(self):
        pass

class TextButton(UIControl):
    def draw(self):
        print("Drawing a textbox")

class Checkbox(UIControl):
    def draw(self):
        print("Drawing a checkbox")

def draw_ui_control(ui_control):
    ui_control.draw()

draw_ui_control(TextButton())
draw_ui_control(Checkbox())
