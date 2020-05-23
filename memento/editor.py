class Editor:
    def __init__(self):
        self.__content = ""
        self.prev_content = []

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.prev_content.append(self.__content)
        self.__content = value

    def undo(self):
        self.__content = self.prev_content.pop()


e = Editor()
e.content = "a"
e.content = "b"
e.content = "c"
e.undo()
e.undo()
print(e.content)