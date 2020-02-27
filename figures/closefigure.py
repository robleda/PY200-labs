from PY200.figures.parent_figure import Figure


class CloseFigure(Figure):
    def __init__(self, *args):
        super().__init__()

        for i in args:
            if isinstance(i, (int, float)):
                continue
            else:
                raise TypeError('All the coordinates must be int or float!')
        if len(args) % 2 != 0:
            raise ValueError('не хватает координат')

        self._points = []
        for i in range(0, len(args), 2):
            self._points.append({'x': args[i], 'y': args[i+1]})

        self.xs = set()
        for i in self._points:
            self.xs.add(i['x'])

        self.ys = set()
        for i in self._points:
            self.ys.add(i['y'])

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, *args):
        for i in args:
            if isinstance(i, (int, float)):
                continue
            else:
                raise TypeError('All the coordinates must be int or float!')
        if len(args) % 2 != 0:
            raise ValueError('не хватает координат')

        self._points = []
        for i in range(len(args), 2):
            self._points.append({'x': args[i], 'y': args[i + 1]})

        self.xs = set()
        for i in self._points:
            self.xs.add(i['x'])

        self.ys = set()
        for i in self._points:
            self.ys.add(i['y'])

    @property
    def x(self):
        return min(self.xs)

    @property
    def y(self):
        return min(self.ys)

    @property
    def width(self):
        return max(self.xs) - min(self.xs)

    @property
    def height(self):
        return max(self.ys) - min(self.ys)

    @property
    def perimeter(self):
        return 2*(self.width + self.height)

    @property
    def square(self):
        return self.width * self.height
