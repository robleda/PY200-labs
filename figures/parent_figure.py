from abc import abstractmethod


class Figure:
    def __init__(self, x=0, y=0):
        self._x = x  # start_x
        self._y = y  # start_y

    @abstractmethod
    def perimeter(self):
        """
        Abstract method
        :return:
        """

    @abstractmethod
    def square(self):
        """
        Abstract method
        :return:
        """

    @abstractmethod
    def width(self):
        """
        Abstract method
        :return:
        """

    @abstractmethod
    def height(self):
        """
        Abstract method
        :return:
        """
