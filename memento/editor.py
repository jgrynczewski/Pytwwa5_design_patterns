class Editor:
    def __init__(self):
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

e = Editor()
e.content = "a"
e.content = "b"
e.content = "c"
e.undo()
print(e.content)