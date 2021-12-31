import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# Import GUI from other file
from Ui_Graph import Ui_Graph


class MainWindow:

    # Initialise the main window when program opened
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Graph()
        self.ui.setupUi(self.main_win)

    def show(self):
        self.main_win.show()


# In case program is run from command line
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
