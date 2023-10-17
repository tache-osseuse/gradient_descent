from forms import Main_Window
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    window = Main_Window()
    app.exec()