import sys
from views.home import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    homeM = MainWindow()
    sys.exit(app.exec())