from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, 
                             QMainWindow, QStyle, QVBoxLayout, QComboBox, 
                             QLineEdit, QHBoxLayout, QMessageBox, QScrollArea,
                             QLabel, QListWidget, QAbstractItemView, QRadioButton, QButtonGroup)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPen, QColor, QBrush
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import random
from algo import RANGE, ITERATIONS

COLOR_MAP = 'cool'

class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.st_plot = fig.add_subplot()
        ax = [i for i in range(-RANGE, RANGE)]
        self.st_plot.contourf(ax, ax, [ax for k in range(2*RANGE)], cmap=COLOR_MAP)
        super(Canvas, self).__init__(fig)

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
    
    def initialize(self):
        self.setWindowTitle('Градиентный спуск')
        self.setFixedSize(QSize(600, 350))
        self.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogResetButton))

        self.graphwidget = Canvas(self, width=5, height=4, dpi=100)
        self.iterations_label = QLabel('Количество итераций:')
        self.iterations_input = QLineEdit()
        self.iterations_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.iterations_input.setReadOnly(True)
        self.iterations_input.setText(str(ITERATIONS))
        self.range_label = QLabel('Диапазон значений x,y:')
        # self.range_label.setStyleSheet('margin-right: 10px')
        self.range_begin_input = QLineEdit()
        self.range_end_input = QLineEdit()
        self.range_begin_input.setMaximumWidth(25)
        self.range_end_input.setMaximumWidth(25)
        self.range_begin_input.setReadOnly(True)
        self.range_end_input.setReadOnly(True)
        self.range_begin_input.setText(str(-RANGE))
        self.range_end_input.setText(str(RANGE))
        self.range_begin_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.range_end_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plot_button = QPushButton('Построение')
        self.plot_button.clicked.connect(self.build_plot_button_clicked)
        self.first_func_label = QLabel('Полином')
        self.first_func_label.setStyleSheet('padding-bottom: 4px')
        self.second_func_label = QLabel('cos(x) + sin(cos(y)*x)')
        self.second_func_label.setStyleSheet('padding-bottom: 2px')
        self.third_func_label = QLabel('x^2 - y^2')
        self.third_func_label.setStyleSheet('padding-bottom: 2px')
        self.point_x_label = QLabel('x:')
        self.point_x_input = QLineEdit()
        self.point_x_input.setMaximumWidth(40)
        self.point_x_input.setReadOnly(True)
        self.point_y_label = QLabel('y:')
        self.point_y_input = QLineEdit()
        self.point_y_input.setMaximumWidth(40)
        self.point_y_input.setReadOnly(True)
        self.random_point_button = QPushButton('Генерация')
        self.random_point_button.clicked.connect(self.generate_button_clicked)
        self.func_radio_buttons = QButtonGroup()
        self.first_func_radio_button = QRadioButton()
        self.second_func_radio_button = QRadioButton()
        self.third_func_radio_button = QRadioButton()

        self.func_radio_buttons.addButton(self.first_func_radio_button)
        self.func_radio_buttons.addButton(self.second_func_radio_button)
        self.func_radio_buttons.addButton(self.third_func_radio_button)

        self.range_layout = QHBoxLayout()
        self.range_layout.addWidget(self.range_label)
        self.range_layout.addWidget(self.range_begin_input, alignment=Qt.AlignmentFlag.AlignLeft)
        self.range_layout.addWidget(self.range_end_input, alignment=Qt.AlignmentFlag.AlignLeft)

        self.iterations_layout = QHBoxLayout()
        self.iterations_layout.addWidget(self.iterations_label)
        self.iterations_layout.addWidget(self.iterations_input)

        self.const_data_layout = QVBoxLayout()
        self.const_data_layout.addLayout(self.range_layout)
        self.const_data_layout.addLayout(self.iterations_layout)

        self.point_layout = QHBoxLayout()
        self.point_layout.addWidget(self.point_x_label)
        self.point_layout.addWidget(self.point_x_input)
        self.point_layout.addWidget(self.point_y_label)
        self.point_layout.addWidget(self.point_y_input)
        self.point_layout.addWidget(self.random_point_button)

        self.first_func_layout = QHBoxLayout()
        self.first_func_layout.addWidget(self.first_func_label)
        self.first_func_layout.addWidget(self.first_func_radio_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.second_func_layout = QHBoxLayout()
        self.second_func_layout.addWidget(self.second_func_label)
        self.second_func_layout.addWidget(self.second_func_radio_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.third_func_layout = QHBoxLayout()
        self.third_func_layout.addWidget(self.third_func_label)
        self.third_func_layout.addWidget(self.third_func_radio_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.radio_buttons_layout = QVBoxLayout()
        self.radio_buttons_layout.setContentsMargins(0, 15, 10, 0)
        self.radio_buttons_layout.addLayout(self.first_func_layout)
        self.radio_buttons_layout.addLayout(self.second_func_layout)
        self.radio_buttons_layout.addLayout(self.third_func_layout)

        self.build_button_layout = QHBoxLayout()
        self.build_button_layout.addWidget(self.plot_button)

        self.plot_layout = QHBoxLayout()
        self.plot_layout.addWidget(self.graphwidget)

        self.data_layout = QVBoxLayout()
        self.data_layout.addLayout(self.const_data_layout)
        self.data_layout.addLayout(self.point_layout)
        self.data_layout.addLayout(self.radio_buttons_layout)
        self.data_layout.addLayout(self.build_button_layout)
        self.data_layout.addStretch()

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.plot_layout)
        self.main_layout.addLayout(self.data_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.show()
    
    def generate_button_clicked(self):
        self.point_x_input.setText(str(random.uniform(-RANGE, RANGE))) 
        self.point_y_input.setText(str(random.uniform(-RANGE, RANGE)))
        self.point_x_input.setCursorPosition(0)
        self.point_y_input.setCursorPosition(0)
    
    def build_plot_button_clicked(self):
        pass

# ax1.contourf(x, y, f, cmap=COLOR_MAP)
# ax1.set_xlabel('x', fontsize = 15)
# ax1.set_ylabel('y', fontsize = 15)
# ax1.scatter(point[0], point[1], c = 'red', marker = '.', s=175)
# ax1.scatter(movin_point[0], movin_point[1], c = 'red', marker = '.', s=175)
# ax1.plot([point[0][0] for point in line], [point[0][1] for point in line], c='red', linestyle='dashed')
