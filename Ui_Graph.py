from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../')
from Ui_Roots import Ui_RootsWindow
from Ui_Intersection import Ui_IntersectionWindow

class Ui_Graph(object):

    def openIntersection(self):
        self.window = QtWidgets.QMainWindow()
        self.uinter = Ui_IntersectionWindow()
        self.uinter.setupUi(self.window)
        self.window.show()
        self.uinter.stackedWidget.setCurrentWidget(self.uinter.home)

        # Setting up buttons - Set up signal (how to pc knows it is clicked) and then slot (what it does)
        self.uinter.pushButton.clicked.connect(self.interoutput)

        # If button is clicked, show the output screen
    def interoutput(self):
        self.uinter.stackedWidget.setCurrentWidget(self.uinter.output)

    def openRoots(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RootsWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        # Setting up buttons - Set up signal (how to pc knows it is clicked) and then slot (what it does)
        self.ui.line_btn.clicked.connect(self.showlinear)
        self.ui.quad_btn.clicked.connect(self.showquadratic)
        self.ui.cube_btn.clicked.connect(self.showcubic)


    def showlinear(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Linear)
        self.ui.lineSolve_btn.clicked.connect(self.rootsoutput)

    def showquadratic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Quadratic)
        self.ui.quadsolve_btn.clicked.connect(self.rootsoutput)

    def showcubic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Cubic)
        self.ui.cubesolve_btn.clicked.connect(self.rootsoutput)

    def rootsoutput(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Output)

    def setupUi(self, Graph):
        Graph.setObjectName("Graph")
        Graph.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(Graph)
        self.centralwidget.setObjectName("centralwidget")
        self.Inputprompt = QtWidgets.QLabel(self.centralwidget)
        self.Inputprompt.setGeometry(QtCore.QRect(10, 10, 451, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Inputprompt.setFont(font)
        self.Inputprompt.setObjectName("Inputprompt")
        self.inputunderline = QtWidgets.QFrame(self.centralwidget)
        self.inputunderline.setGeometry(QtCore.QRect(10, 70, 431, 16))
        self.inputunderline.setFrameShape(QtWidgets.QFrame.HLine)
        self.inputunderline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.inputunderline.setObjectName("inputunderline")
        self.graphspace = QtWidgets.QLabel(self.centralwidget)
        self.graphspace.setGeometry(QtCore.QRect(460, 10, 521, 461))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.graphspace.setFont(font)
        self.graphspace.setAlignment(QtCore.Qt.AlignCenter)
        self.graphspace.setObjectName("graphspace")
        self.eq1input = QtWidgets.QLineEdit(self.centralwidget)
        self.eq1input.setGeometry(QtCore.QRect(55, 100, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eq1input.setFont(font)
        self.eq1input.setText("")
        self.eq1input.setObjectName("eq1input")
        self.eq2input = QtWidgets.QLineEdit(self.centralwidget)
        self.eq2input.setGeometry(QtCore.QRect(55, 150, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eq2input.setFont(font)
        self.eq2input.setObjectName("eq2input")
        self.eq3input = QtWidgets.QLineEdit(self.centralwidget)
        self.eq3input.setGeometry(QtCore.QRect(55, 200, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eq3input.setFont(font)
        self.eq3input.setObjectName("eq3input")
        self.eq4input = QtWidgets.QLineEdit(self.centralwidget)
        self.eq4input.setGeometry(QtCore.QRect(55, 250, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eq4input.setFont(font)
        self.eq4input.setObjectName("eq4input")
        self.eq5input = QtWidgets.QLineEdit(self.centralwidget)
        self.eq5input.setGeometry(QtCore.QRect(55, 300, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eq5input.setFont(font)
        self.eq5input.setObjectName("eq5input")
        self.plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plot_btn.setGeometry(QtCore.QRect(320, 350, 121, 115))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plot_btn.setFont(font)
        self.plot_btn.setObjectName("plot_btn")
        self.roots_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openRoots())
        self.roots_btn.setGeometry(QtCore.QRect(5, 350, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.roots_btn.setFont(font)
        self.roots_btn.setObjectName("roots_btn")
        self.Intersection_btn = QtWidgets.QPushButton(self.centralwidget, clicked  = lambda: self.openIntersection())
        self.Intersection_btn.setGeometry(QtCore.QRect(5, 425, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Intersection_btn.setFont(font)
        self.Intersection_btn.setObjectName("Intersection_btn")
        self.Y1label = QtWidgets.QLabel(self.centralwidget)
        self.Y1label.setGeometry(QtCore.QRect(5, 100, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Y1label.setFont(font)
        self.Y1label.setObjectName("Y1label")
        self.Y2label = QtWidgets.QLabel(self.centralwidget)
        self.Y2label.setGeometry(QtCore.QRect(5, 150, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Y2label.setFont(font)
        self.Y2label.setObjectName("Y2label")
        self.Y3label = QtWidgets.QLabel(self.centralwidget)
        self.Y3label.setGeometry(QtCore.QRect(5, 200, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Y3label.setFont(font)
        self.Y3label.setObjectName("Y3label")
        self.Y4label = QtWidgets.QLabel(self.centralwidget)
        self.Y4label.setGeometry(QtCore.QRect(5, 250, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Y4label.setFont(font)
        self.Y4label.setObjectName("Y4label")
        self.Y5label = QtWidgets.QLabel(self.centralwidget)
        self.Y5label.setGeometry(QtCore.QRect(5, 300, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Y5label.setFont(font)
        self.Y5label.setObjectName("Y5label")
        Graph.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Graph)
        self.statusbar.setObjectName("statusbar")
        Graph.setStatusBar(self.statusbar)

        self.retranslateUi(Graph)
        QtCore.QMetaObject.connectSlotsByName(Graph)

    def retranslateUi(self, Graph):
        _translate = QtCore.QCoreApplication.translate
        Graph.setWindowTitle(_translate("Graph", "Graph"))
        self.Inputprompt.setText(_translate("Graph", "Enter equation in the form Y = f(x)"))
        self.graphspace.setText(_translate("Graph", "The graph will be here"))
        self.plot_btn.setText(_translate("Graph", "Plot"))
        self.roots_btn.setText(_translate("Graph", "Roots"))
        self.Intersection_btn.setText(_translate("Graph", "Intersection "))
        self.Y1label.setText(_translate("Graph", "Y = "))
        self.Y2label.setText(_translate("Graph", "Y = "))
        self.Y3label.setText(_translate("Graph", "Y = "))
        self.Y4label.setText(_translate("Graph", "Y = "))
        self.Y5label.setText(_translate("Graph", "Y = "))

