from PyQt5 import QtCore, QtGui, QtWidgets
from fractions import Fraction
import math
import numpy as np


class Ui_IntersectionWindow(object):

    # When the user clicks solve, this executes
    def clicksolve(self):
        # If input is empty, take it as 0
        if self.A1input.text() == '':
            self.A1input.setText('0')
        if self.B1input.text() == '':
            self.B1input.setText('0')
        if self.C1input.text() == '':
            self.C1input.setText('0')
        if self.D1input.text() == '':
            self.D1input.setText('0')
        # Convert the first equation into float form to aid further calculation
        a1 = float(Fraction(self.A1input.text()))
        b1 = float(Fraction(self.B1input.text()))
        c1 = float(Fraction(self.C1input.text()))
        d1 = float(Fraction(self.D1input.text()))

        # If input is empty, take it as 0
        if self.A2input.text() == '':
            self.A2input.setText('0')
        if self.B2input.text() == '':
            self.B2input.setText('0')
        if self.C2input.text() == '':
            self.C2input.setText('0')
        if self.D2input.text() == '':
            self.D2input.setText('0')

        # Convert the first equation into float form to aid further calculation
        a2 = float(Fraction(self.A2input.text()))
        b2 = float(Fraction(self.B2input.text()))
        c2 = float(Fraction(self.C2input.text()))
        d2 = float(Fraction(self.D2input.text()))
        # Finding the resultant equation
        x3 = a1 - a2
        x2 = b1 - b2
        x = c1 - c2
        c = d1 - d2

        if x3 == 0 and x2 == 0 and x == 0 and c == 0:
            self.intersectionlabel.setText('The lines are coincident')

        while x3 != 0 or x2 != 0 or x != 0 or c != 0:
            # If the resultant equation is linear
            if x3 == 0 and x2 == 0:
                x_inter = round((c / -x), 3)
                y_inter = round((a1 * x_inter ** 3 + b1 * x_inter ** 2 + c1 * x_inter + d1), 3)
                self.intersectionlabel.setText(f'Intersection: ({x_inter},{y_inter})')

            # If the resultant equation is quadratic
            elif x3 == 0:
                # Find the discriminant
                dis = x * x - 4 * x2 * c
                sqrt_val = math.sqrt(abs(dis))

                # checking condition for discriminant
                if dis > 0:
                    xinter1 = round((-x + sqrt_val) / (2 * x2), 3)
                    yinter1 = round((a1 * xinter1 ** 3 + b1 * xinter1 ** 2 + c1 * xinter1 + d1), 3)
                    xinter2 = round((-x - sqrt_val) / (2 * x2), 3)
                    yinter2 = round((a1 * xinter2 ** 3 + b1 * xinter2 ** 2 + c1 * xinter2 + d1), 3)
                    self.intersectionlabel.setText(f'Intersection: ({xinter1},{yinter1}), ({xinter2},{yinter2})')

                elif dis == 0:
                    xinter = round((-x / (2 * x2)), 3)
                    yinter = round((a1 * xinter ** 3 + b1 * xinter ** 2 + c1 * xinter + d1), 3)
                    self.intersectionlabel.setText(f'Intersection: ({xinter},{yinter})')

                # If roots are complex, that means no intersection between the 2 equations inputted
                elif dis < 0:
                    self.intersectionlabel.setText('No intersection')

            # If the resultant equation is cubic
            elif x3 != 0:
                coeff = [x3, x2, x, c]

                # Using numpy to find the roots and then rounding them to 3 decimal places
                intersection = np.roots(coeff)
                roundedinter = np.around(intersection, 3)

                # Outputting the roots as a string and saving them to variables
                x = str(roundedinter[0])
                y = str(roundedinter[1])
                z = str(roundedinter[2])

                # If complex part is 0, get rid of it
                x = x.replace('+0j', '')
                y = y.replace('+0j', '')
                z = z.replace('+0j', '')

                # Checking if variable has a complex part and if not, adding it to an array
                realarr = []
                comparr = []
                if 'j' not in x:
                    realarr.append(x)
                if 'j' not in y:
                    realarr.append(y)
                if 'j' not in z:
                    realarr.append(z)

                while len(realarr) != 0:
                    # If length of array is 1, only 1 real root
                    if len(realarr) == 1:
                        xinter = realarr[0]
                        xinter = float(xinter[1:-1])
                        inter = xinter, round(a1 * xinter ** 3 + b1 * xinter ** 2 + c1 * xinter + d1, 3)
                        self.intersectionlabel.setText(f'Intersection: {inter}')
                        break

                    elif len(realarr) == 3:
                        # If length of array is 3, 3 real roots
                        xinter1 = realarr[0]
                        if xinter1 == '.':
                            xinter1 = 0.0
                        elif xinter1 != 0.0:
                            xinter1 = float(xinter1)
                        inter1 = xinter1, round(a1 * xinter1 ** 3 + b1 * xinter1 ** 2 + c1 * xinter1 + d1, 3)

                        xinter2 = realarr[1]
                        if xinter2 == '.':
                            xinter2 = 0.0
                        elif xinter2 != 0.0:
                            xinter2 = float(xinter2)
                        inter2 = xinter2, round(a1 * xinter2 ** 3 + b1 * xinter2 ** 2 + c1 * xinter2 + d1, 3)

                        xinter3 = realarr[2]
                        if xinter3 == '.':
                            xinter3 = 0.0
                        elif xinter3 != 0.0:
                            xinter3 = float(xinter3)
                        inter3 = xinter3, round(a1 * xinter3 ** 3 + b1 * xinter3 ** 2 + c1 * xinter3 + d1, 3)

                        self.intersectionlabel.setText(f'Intersections: {inter1}, {inter2}, {inter3}')
                        break
            break

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 10, 761, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.inputprompt = QtWidgets.QLabel(self.home)
        self.inputprompt.setGeometry(QtCore.QRect(40, 20, 681, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.inputprompt.setFont(font)
        self.inputprompt.setObjectName("inputprompt")
        self.eq1label = QtWidgets.QLabel(self.home)
        self.eq1label.setGeometry(QtCore.QRect(100, 170, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eq1label.setFont(font)
        self.eq1label.setObjectName("eq1label")
        self.eq2label = QtWidgets.QLabel(self.home)
        self.eq2label.setGeometry(QtCore.QRect(100, 350, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eq2label.setFont(font)
        self.eq2label.setObjectName("eq2label")
        self.A1input = QtWidgets.QLineEdit(self.home)
        self.A1input.setGeometry(QtCore.QRect(140, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.A1input.setFont(font)
        self.A1input.setAlignment(QtCore.Qt.AlignCenter)
        self.A1input.setObjectName("A1input")
        self.A2input = QtWidgets.QLineEdit(self.home)
        self.A2input.setGeometry(QtCore.QRect(140, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.A2input.setFont(font)
        self.A2input.setAlignment(QtCore.Qt.AlignCenter)
        self.A2input.setObjectName("A2input")
        self.B1input = QtWidgets.QLineEdit(self.home)
        self.B1input.setGeometry(QtCore.QRect(260, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.B1input.setFont(font)
        self.B1input.setAlignment(QtCore.Qt.AlignCenter)
        self.B1input.setObjectName("B1input")
        self.B2input = QtWidgets.QLineEdit(self.home)
        self.B2input.setGeometry(QtCore.QRect(260, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.B2input.setFont(font)
        self.B2input.setAlignment(QtCore.Qt.AlignCenter)
        self.B2input.setObjectName("B2input")
        self.C1input = QtWidgets.QLineEdit(self.home)
        self.C1input.setGeometry(QtCore.QRect(390, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.C1input.setFont(font)
        self.C1input.setAlignment(QtCore.Qt.AlignCenter)
        self.C1input.setObjectName("C1input")
        self.C2input = QtWidgets.QLineEdit(self.home)
        self.C2input.setGeometry(QtCore.QRect(390, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.C2input.setFont(font)
        self.C2input.setAlignment(QtCore.Qt.AlignCenter)
        self.C2input.setObjectName("C2input")
        self.D1input = QtWidgets.QLineEdit(self.home)
        self.D1input.setGeometry(QtCore.QRect(500, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.D1input.setFont(font)
        self.D1input.setAlignment(QtCore.Qt.AlignCenter)
        self.D1input.setObjectName("D1input")
        self.D2input = QtWidgets.QLineEdit(self.home)
        self.D2input.setGeometry(QtCore.QRect(500, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.D2input.setFont(font)
        self.D2input.setAlignment(QtCore.Qt.AlignCenter)
        self.D2input.setObjectName("D2input")
        self.pushButton = QtWidgets.QPushButton(self.home, clicked=lambda: self.clicksolve())
        self.pushButton.setGeometry(QtCore.QRect(570, 460, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.home)
        self.output = QtWidgets.QWidget()
        self.output.setObjectName("output")
        self.outputprompt = QtWidgets.QLabel(self.output)
        self.outputprompt.setGeometry(QtCore.QRect(60, 10, 600, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.outputprompt.setFont(font)
        self.outputprompt.setObjectName("outputprompt")
        self.intersectionlabel = QtWidgets.QLabel(self.output)
        self.intersectionlabel.setGeometry(QtCore.QRect(10, 240, 741, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.intersectionlabel.setFont(font)
        self.intersectionlabel.setObjectName("intersectionlabel")
        self.stackedWidget.addWidget(self.output)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Intersection", "Intersection"))
        self.inputprompt.setText(_translate("MainWindow", "Please input equation 1 and equation 2 below:"))
        self.eq1label.setText(_translate("MainWindow", "Y=     X³ +      X² +      X +   "))
        self.eq2label.setText(_translate("MainWindow", "Y=     X³ +      X² +      X +   "))
        self.A1input.setPlaceholderText(_translate("MainWindow", "a1"))
        self.A2input.setPlaceholderText(_translate("MainWindow", "a2"))
        self.B1input.setPlaceholderText(_translate("MainWindow", "b1"))
        self.B2input.setPlaceholderText(_translate("MainWindow", "b2"))
        self.C1input.setPlaceholderText(_translate("MainWindow", "c1"))
        self.C2input.setPlaceholderText(_translate("MainWindow", "c2"))
        self.D1input.setPlaceholderText(_translate("MainWindow", "d1"))
        self.D2input.setPlaceholderText(_translate("MainWindow", "d2"))
        self.pushButton.setText(_translate("MainWindow", "Solve"))
        self.outputprompt.setText(_translate("MainWindow", "The intersection between the 2 equations are:"))
        self.intersectionlabel.setText(_translate("MainWindow", "Intersections:"))
