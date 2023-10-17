from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, 
                             QMainWindow, QStyle, QVBoxLayout, QComboBox, 
                             QLineEdit, QHBoxLayout, QMessageBox, QScrollArea,
                             QLabel, QListWidget, QAbstractItemView, QRadioButton, QButtonGroup)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPen, QColor, QBrush
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

COLOR_MAP = 'cool'

class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.plot = fig.add_subplot()
        self.plot.contourf([1,3], [3,4], [[10,12],[34,21]], cmap=COLOR_MAP)
        super(Canvas, self).__init__(fig)

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
    
    def initialize(self):
        self.setWindowTitle('Градиентный спуск')
        self.setFixedSize(QSize(500, 350))
        self.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogResetButton))

        self.graphwidget = Canvas(self, width=5, height=4, dpi=100)

        self.plot_layout = QHBoxLayout()
        self.plot_layout.addWidget(self.graphwidget)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.plot_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.show()