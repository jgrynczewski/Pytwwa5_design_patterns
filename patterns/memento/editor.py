#Originator
class Editor:
    def __init__(self):
        self.__content = ""
        self.prev_content = []

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.prev_content.append(EditorState(self.__content))
        self.__content = value

    def create_state(self):
        return EditorState(self.__content)

    def restore(self, state):
        self.__content = state.content

# Memento
class EditorState:
    def __init__(self, content):
        self.__content = content

    @property
    def content(self):
        return self.__content

# Caretaker
class History:
    def __init__(self):
        self.__states = []

    def push(self, state: EditorState):
        self.__states.append(state)

    def pop(self) -> EditorState:
        return self.__states.pop()

e = Editor()
h = History()

e.content = "a"
h.push(e.create_state())

e.content = "b"
h.push(e.create_state())

e.content = "c"

e.restore(h.pop())
e.restore(h.pop())

print(e.content)
