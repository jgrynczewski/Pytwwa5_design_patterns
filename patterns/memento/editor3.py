import abc


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

    def create_state(self, editor_state):
        return editor_state(self.__content)

    def restore(self, state):
        self.__content = state.content

# Abstract Memento
class AbstractEditorState(abc.ABC):

    @property
    @abc.abstractmethod
    def content(self):
        pass


# Concrete Memento
class EditorState(AbstractEditorState):
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
h.push(e.create_state(EditorState))

e.content = "b"
h.push(e.create_state(EditorState))

e.content = "c"

e.restore(h.pop())
e.restore(h.pop())

print(e.content)
