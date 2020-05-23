# DZIEDZICZENIE - DRY Don't Repeate Yourself

class UIControl:
    def enable(self):
        print("Enable")

class TextButton(UIControl):
    pass

t = TextButton()
t.enable()