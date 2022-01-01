import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# Import GUI from other file
from Ui_Intersection import Ui_MainWindow


class MainWindow:

    # Initialise the main window when program opened
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Which page is home
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # Setting up buttons - Set up signal (how to pc knows it is clicked) and then slot (what it does)
        self.ui.pushButton.clicked.connect(self.showoutput)

    def show(self):
        self.main_win.show()

    # If button is clicked, show the output screen
    def showoutput(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.output)


# In case program is run from command line
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
