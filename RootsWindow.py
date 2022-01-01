import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# Import GUI from other file
from Ui_Roots import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Which page is home
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        # Setting up buttons - Set up signal (how to pc knows it is clicked) and then slot (what it does)
        self.ui.line_btn.clicked.connect(self.showlinear)
        self.ui.quad_btn.clicked.connect(self.showquadratic)
        self.ui.cube_btn.clicked.connect(self.showcubic)

    def show(self):
        self.main_win.show()

    def showlinear(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Linear)
        self.ui.lineSolve_btn.clicked.connect(self.showoutput)

    def showquadratic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Quadratic)
        self.ui.quadsolve_btn.clicked.connect(self.showoutput)

    def showcubic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Cubic)
        self.ui.cubesolve_btn.clicked.connect(self.showoutput)

    def showoutput(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Output)


# In case program is run from command line
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
