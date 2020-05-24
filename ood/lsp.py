# LSP - Zasada podstawień Liskova

class Rectange:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self._width}, height: {self._height}"

class Square(Rectange):
    def __init__(self, size):
        Rectange.__init__(self, size, size)

    @Rectange.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectange.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):
    w = rc.width # 5, 5
    rc.height = 10 # 10, 10

    expected_value = 10*w
    print(f"Spodziewaliśmy się: {expected_value}, otrzymaliśmy {rc.area}")


rc = Rectange(2, 3)
sq = Square(5)
use_it(sq)
