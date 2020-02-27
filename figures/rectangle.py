from PY200.figures.parent_figure import Figure


class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x, y)
        self._w = w
        self._h = h

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError('Coordinate must be int or float!')
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError('Coordinate must be int or float!')
        self._y = y

    @property
    def perimeter(self):
        return 2*(self._w + self._h)

    @property
    def square(self):
        return self._w * self._h

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, w):
        if not isinstance(w, (int, float)):
            raise TypeError('Width must be int or float!')
        self._w = w

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, h):
        if not isinstance(h, (int, float)):
            raise TypeError('Height must be int or float!')
        self._h = h
