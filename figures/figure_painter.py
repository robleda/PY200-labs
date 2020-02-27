import os
import sys

from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtWidgets import QApplication, QWidget

from PY200.figures.ellipse import Ellipse
from PY200.figures.rectangle import Rectangle
from PY200.figures.closefigure import CloseFigure
from PY200.figures.parent_figure import Figure

#
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\PySide2\\plugins\\platforms'
sys.path.append(os.path.abspath(os.getcwd()))


class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []

    def set_figures(self, figures):
        self.__figures = figures

    def paintEvent(self, event):
        painter = QPainter(self)
        reset_brush = painter.brush()
        for figure in self.__figures:
            if not isinstance(figure, Figure):
                raise TypeError

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x, figure.y,
                                 figure.width, figure.height)
                continue

            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.x, figure.y, figure.width, figure.height)
                continue

            if isinstance(figure, CloseFigure):
                painter.setBrush(QBrush(Qt.blue))

                points = []
                for point in figure.points:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # список фигур
    figures = [Rectangle(50, 50, 50, 100), Ellipse(100, 50, 300, 50),
               CloseFigure(200, 300, 200, 9, 550, 450, 400, 100)]

    figure_widget.set_figures(figures)

    figure_widget.show()
    sys.exit(app.exec_())
