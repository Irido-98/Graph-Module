from fractions import Fraction
import math
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RootsWindow(object):

    def clickline(self):
        if self.Alineinput.text() == '':
            self.Alineinput.setText('0')
        if self.Blineinput.text() == '':
            self.Blineinput.setText('0')
        a = float(Fraction(self.Alineinput.text()))
        b = float(Fraction(self.Blineinput.text()))
        self.yinterceptlabel.setText(f'Y-intercept:(0.0, {b})')
        self.turningpointslabel.setText('Linear equation has no turning points')
        if a == 0 and b == 0:
            roots = 'Infinite roots'
            self.rootslabel.setText(f'Roots: {roots}')
        elif a == 0:
            roots = 'No roots'
            self.rootslabel.setText(f'Roots: {roots}')
        elif a != 0:
            x_root = round((b / -a), 3)
            if x_root == -0.0:
                x_root = 0.0
            roots = x_root, 0.0
            self.rootslabel.setText(f'Roots: {roots}')

    def clickquad(self):
        if self.Aquadinput.text() == '':
            self.Aquadinput.setText('0')
        if self.Bquadinput.text() == '':
            self.Bquadinput.setText('0')
        if self.Cquadinput.text() == '':
            self.Cquadinput.setText('0')
        a = float(Fraction(self.Aquadinput.text()))
        b = float(Fraction(self.Bquadinput.text()))
        c = float(Fraction(self.Cquadinput.text()))
        dis = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis))
        self.yinterceptlabel.setText(f'Y-intercept: (0.0, {c})')
        if a == 0 and b == 0 and c == 0:
            self.rootslabel.setText("You didn't enter an equation")
            self.yinterceptlabel.setText('')
            self.turningpointslabel.setText('')

        while a != 0 or b != 0 or c != 0:
            # If a is 0, then tell user to use linear solver
            if a == 0:
                self.rootslabel.setText('Run linear solver to solve this equation ')
                self.yinterceptlabel.setText('')
                self.turningpointslabel.setText('')

            elif a != 0:
                # Differential of quadratic
                x = 2 * a
                y = b
                # Finding the roots of the differential
                dx_root = round((y / -x), 3)
                # Since -0.0 is not correct math syntax
                if dx_root == -0.0:
                    dx_root = 0.0
                dy_root = round((a * (dx_root ** 2) + b * dx_root + c), 3)
                self.turningpointslabel.setText(f'Turning points: ({dx_root},{dy_root})')

                # checking condition for discriminant
                if dis > 0:
                    root1 = (round((-b + sqrt_val) / (2 * a), 3), 0.0)
                    root2 = (round((-b - sqrt_val) / (2 * a), 3), 0.0)
                    if root1 == (-0.0, 0.0):
                        root1 = (0.0, 0.0)
                    elif root2 == (-0.0, 0.0):
                        root2 = (0.0, 0.0)
                    self.rootslabel.setText(f'Distinct roots: {root1}, {root2}')

                elif dis == 0:
                    root = round((-b / (2 * a)), 3)
                    if root == -0.0:
                        root = 0.0
                    self.rootslabel.setText(f'Repeated roots: ({root},0.0)')

                # when discriminant is less than 0. Complex roots
                else:
                    root = round(- b / (2 * a), 3)
                    imagroot = round(sqrt_val / (2 * a), 3)
                    self.rootslabel.setText(f'Complex roots: {root}+{imagroot}i, {root}-{imagroot}i')
            break

    def clickcube(self):
        if self.Acubeinput.text() == '':
            self.Acubeinput.setText('0')
        if self.Bcubeinput.text() == '':
            self.Bcubeinput.setText('0')
        if self.Ccubeinput.text() == '':
            self.Ccubeinput.setText('0')
        if self.Dcubeinput.text() == '':
            self.Dcubeinput.setText('0')
        a = float(Fraction(self.Acubeinput.text()))
        b = float(Fraction(self.Bcubeinput.text()))
        c = float(Fraction(self.Ccubeinput.text()))
        d = float(Fraction(self.Dcubeinput.text()))

        if a == 0 and b == 0 and c == 0 and d == 0:
            self.rootslabel.setText("You didn't enter an equation")
            self.yinterceptlabel.setText('')
            self.turningpointslabel.setText('')

        while a != 0 or b != 0 or c != 0 or d != 0:
            # Check to see input is actually a cubic
            if a == 0 and b != 0:
                self.rootslabel.setText('Run quadratic solver to solve this equation ')
                self.yinterceptlabel.setText('')
                self.turningpointslabel.setText('')
            elif a == 0 and b == 0:
                self.rootslabel.setText('Run linear solver to solve this equation ')
                self.yinterceptlabel.setText('')
                self.turningpointslabel.setText('')

            if a != 0:
                self.yinterceptlabel.setText(f'Y-intercept: (0.0,{d})')
                # First order differential
                x = 3 * a ** 2
                y = 2 * b
                z = c
                dis = y * y - 4 * x * z
                sqrt_val = math.sqrt(abs(dis))

                # If first differential has discrete roots, there are always 2 turning points
                if dis > 0:
                    turnx1 = round((-y + sqrt_val) / (2 * x), 3)
                    turnx2 = round((-y - sqrt_val) / (2 * x), 3)
                    # Finding the x coord of turning points
                    if turnx1 == -0.0:
                        turnx1 = 0.0
                    elif turnx2 == -0.0:
                        turnx2 = 0.0
                    # Finding the y coord of turning points
                    turny1 = round((a * turnx1 ** 3) + (b * turnx1 ** 2) + (c * turnx1) + d, 3)
                    turny2 = round(((a * turnx2 ** 3) + (b * turnx2 ** 2) + (c * turnx2) + d), 3)
                    turnpoint1 = (turnx1, turny1)
                    turnpoint2 = (turnx2, turny2)
                    self.turningpointslabel.setText(f'Turning points: {turnpoint1}, {turnpoint2}')

                # If first differential has repeated roots, there is only one stationary point of inflection
                elif dis == 0:
                    inflectionx = round((-y / (2 * x)), 3)
                    # Finding x coord of inflection point
                    if inflectionx == -0.0:
                        inflectionx = 0.0
                    # Finding y coord of inflection point
                    inflectiony = round((a * inflectionx ** 3) + (b * inflectionx ** 2) + (c * inflectionx) + d, 3)
                    inflectionpoint = (inflectionx, inflectiony)
                    self.turningpointslabel.setText(f'Stationary point of inflection: {inflectionpoint}')

                # If first differential has complex roots, there are 1 or 2 points of inflection
                else:
                    self.turningpointslabel.setText('No turning points, only 1 point of inflection ')

                # Function only takes in arrays
                coeff = [a, b, c, d]
                # Using numpy to find the roots and then rounding them to 3 decimal places
                roots = np.roots(coeff)
                roundedroots = np.around(roots, 3)
                # Outputting the roots as a string and saving them to variables
                x = str(roundedroots[0])
                y = str(roundedroots[1])
                z = str(roundedroots[2])

                # If complex part is 0, get rid of it
                x = x.replace('+0j', '')
                y = y.replace('+0j', '')
                z = z.replace('+0j', '')

                # Checking if variable has a complex part and if not, adding it to an array
                realarr = []
                comparr = []
                if 'j' not in x:
                    realarr.append(x)
                else:
                    comparr.append(x)
                if 'j' not in y:
                    realarr.append(y)
                else:
                    comparr.append(y)
                if 'j' not in z:
                    realarr.append(z)
                else:
                    comparr.append(z)

                while len(realarr) != 0:
                    # If length of array is 1, only 1 real root
                    if len(realarr) == 1:
                        xroot = realarr[0]
                        xroot = float(xroot[1:-1])
                        root = xroot, 0.0
                        self.rootslabel.setText(f'Roots: {root}, {comparr[0]}, {comparr[1]}')
                        break

                    elif len(realarr) == 3:

                        xroot1 = realarr[0]
                        if xroot1 == '.':
                            xroot1 = 0.0
                        elif xroot1 != 0.0:
                            xroot1 = float(xroot1)
                        root1 = xroot1, 0.0

                        xroot2 = realarr[1]
                        if xroot2 == '.':
                            xroot2 = 0.0
                        elif xroot2 != 0.0:
                            xroot2 = float(xroot2)
                        root2 = xroot2, 0.0

                        xroot3 = realarr[2]
                        if xroot3 == '.':
                            xroot3 = 0.0
                        elif xroot3 != 0.0:
                            xroot3 = float(xroot3)
                        root3 = xroot3, 0.0

                        self.rootslabel.setText(f'Roots: {root1}, {root2}, {root3}')
                        break
            break

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.line_btn = QtWidgets.QPushButton(self.Home)
        self.line_btn.setGeometry(QtCore.QRect(300, 125, 151, 51))
        self.line_btn.setObjectName("line_btn")
        self.quad_btn = QtWidgets.QPushButton(self.Home)
        self.quad_btn.setGeometry(QtCore.QRect(300, 250, 151, 51))
        self.quad_btn.setObjectName("quad_btn")
        self.cube_btn = QtWidgets.QPushButton(self.Home)
        self.cube_btn.setGeometry(QtCore.QRect(300, 375, 151, 51))
        self.cube_btn.setObjectName("cube_btn")
        self.prompt = QtWidgets.QLabel(self.Home)
        self.prompt.setGeometry(QtCore.QRect(130, 20, 500, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prompt.setFont(font)
        self.prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.prompt.setObjectName("prompt")
        self.stackedWidget.addWidget(self.Home)
        self.Linear = QtWidgets.QWidget()
        self.Linear.setMinimumSize(QtCore.QSize(800, 600))
        self.Linear.setMaximumSize(QtCore.QSize(800, 600))
        self.Linear.setObjectName("Linear")
        self.lineSolve_btn = QtWidgets.QPushButton(self.Linear, clicked=lambda: self.clickline())
        self.lineSolve_btn.setGeometry(QtCore.QRect(550, 420, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineSolve_btn.setFont(font)
        self.lineSolve_btn.setObjectName("lineSolve_btn")
        self.Linearprompt = QtWidgets.QLabel(self.Linear)
        self.Linearprompt.setGeometry(QtCore.QRect(160, 10, 491, 181))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Linearprompt.setFont(font)
        self.Linearprompt.setWordWrap(True)
        self.Linearprompt.setObjectName("Linearprompt")
        self.quadinputprompt_2 = QtWidgets.QLabel(self.Linear)
        self.quadinputprompt_2.setGeometry(QtCore.QRect(220, 250, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.quadinputprompt_2.setFont(font)
        self.quadinputprompt_2.setObjectName("quadinputprompt_2")
        self.Alineinput = QtWidgets.QLineEdit(self.Linear)
        self.Alineinput.setGeometry(QtCore.QRect(270, 265, 51, 51))
        a = self.Alineinput.text()
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Alineinput.setFont(font)
        self.Alineinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Alineinput.setObjectName("Alineinput")
        self.Blineinput = QtWidgets.QLineEdit(self.Linear)
        self.Blineinput.setGeometry(QtCore.QRect(375, 265, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Blineinput.setFont(font)
        self.Blineinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Blineinput.setObjectName("Blineinput")
        self.stackedWidget.addWidget(self.Linear)
        self.Quadratic = QtWidgets.QWidget()
        self.Quadratic.setObjectName("Quadratic")
        self.quadsolve_btn = QtWidgets.QPushButton(self.Quadratic, clicked=lambda: self.clickquad())
        self.quadsolve_btn.setGeometry(QtCore.QRect(570, 430, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quadsolve_btn.setFont(font)
        self.quadsolve_btn.setObjectName("quadsolve_btn")
        self.Quadraticprompt = QtWidgets.QLabel(self.Quadratic)
        self.Quadraticprompt.setGeometry(QtCore.QRect(150, 30, 491, 181))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Quadraticprompt.setFont(font)
        self.Quadraticprompt.setAlignment(QtCore.Qt.AlignCenter)
        self.Quadraticprompt.setWordWrap(True)
        self.Quadraticprompt.setObjectName("Quadraticprompt")
        self.quadinputprompt = QtWidgets.QLabel(self.Quadratic)
        self.quadinputprompt.setGeometry(QtCore.QRect(150, 280, 551, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.quadinputprompt.setFont(font)
        self.quadinputprompt.setObjectName("quadinputprompt")
        self.Aquadinput = QtWidgets.QLineEdit(self.Quadratic)
        self.Aquadinput.setGeometry(QtCore.QRect(200, 295, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Aquadinput.setFont(font)
        self.Aquadinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Aquadinput.setObjectName("Aquadinput")
        self.Bquadinput = QtWidgets.QLineEdit(self.Quadratic)
        self.Bquadinput.setGeometry(QtCore.QRect(325, 295, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Bquadinput.setFont(font)
        self.Bquadinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Bquadinput.setObjectName("Bquadinput")
        self.Cquadinput = QtWidgets.QLineEdit(self.Quadratic)
        self.Cquadinput.setGeometry(QtCore.QRect(450, 295, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Cquadinput.setFont(font)
        self.Cquadinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Cquadinput.setObjectName("Cquadinput")
        self.stackedWidget.addWidget(self.Quadratic)
        self.Cubic = QtWidgets.QWidget()
        self.Cubic.setObjectName("Cubic")
        self.cubesolve_btn = QtWidgets.QPushButton(self.Cubic, clicked=lambda: self.clickcube())
        self.cubesolve_btn.setGeometry(QtCore.QRect(620, 440, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cubesolve_btn.setFont(font)
        self.cubesolve_btn.setObjectName("cubesolve_btn")
        self.Cubicprompt = QtWidgets.QLabel(self.Cubic)
        self.Cubicprompt.setGeometry(QtCore.QRect(150, 10, 491, 235))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Cubicprompt.setFont(font)
        self.Cubicprompt.setAlignment(QtCore.Qt.AlignCenter)
        self.Cubicprompt.setWordWrap(True)
        self.Cubicprompt.setObjectName("Cubicprompt")
        self.cubeinputprompt = QtWidgets.QLabel(self.Cubic)
        self.cubeinputprompt.setGeometry(QtCore.QRect(175, 260, 751, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cubeinputprompt.setFont(font)
        self.cubeinputprompt.setObjectName("cubeinputprompt")
        self.Acubeinput = QtWidgets.QLineEdit(self.Cubic)
        self.Acubeinput.setGeometry(QtCore.QRect(225, 285, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Acubeinput.setFont(font)
        self.Acubeinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Acubeinput.setObjectName("Acubeinput")
        self.Bcubeinput = QtWidgets.QLineEdit(self.Cubic)
        self.Bcubeinput.setGeometry(QtCore.QRect(343, 285, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Bcubeinput.setFont(font)
        self.Bcubeinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Bcubeinput.setObjectName("Bcubeinput")
        self.Ccubeinput = QtWidgets.QLineEdit(self.Cubic)
        self.Ccubeinput.setGeometry(QtCore.QRect(462, 285, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Ccubeinput.setFont(font)
        self.Ccubeinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Ccubeinput.setObjectName("Ccubeinput")
        self.Dcubeinput = QtWidgets.QLineEdit(self.Cubic)
        self.Dcubeinput.setGeometry(QtCore.QRect(565, 285, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Dcubeinput.setFont(font)
        self.Dcubeinput.setAlignment(QtCore.Qt.AlignCenter)
        self.Dcubeinput.setObjectName("Dcubeinput")
        self.stackedWidget.addWidget(self.Cubic)
        self.Output = QtWidgets.QWidget()
        self.Output.setObjectName("Output")
        self.Solutionprompt = QtWidgets.QLabel(self.Output)
        self.Solutionprompt.setGeometry(QtCore.QRect(100, 20, 700, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Solutionprompt.setFont(font)
        self.Solutionprompt.setObjectName("Solutionprompt")
        self.rootslabel = QtWidgets.QLabel(self.Output)
        self.rootslabel.setGeometry(QtCore.QRect(40, 120, 731, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rootslabel.setFont(font)
        self.rootslabel.setObjectName("rootslabel")
        self.yinterceptlabel = QtWidgets.QLabel(self.Output)
        self.yinterceptlabel.setGeometry(QtCore.QRect(40, 230, 731, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yinterceptlabel.setFont(font)
        self.yinterceptlabel.setObjectName("yinterceptlabel")
        self.turningpointslabel = QtWidgets.QLabel(self.Output)
        self.turningpointslabel.setGeometry(QtCore.QRect(40, 350, 731, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.turningpointslabel.setFont(font)
        self.turningpointslabel.setObjectName("turningpointslabel")
        self.stackedWidget.addWidget(self.Output)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Roots", "Roots"))
        self.line_btn.setText(_translate("MainWindow", "Linear Solver"))
        self.quad_btn.setText(_translate("MainWindow", "Quadratic Solver"))
        self.cube_btn.setText(_translate("MainWindow", "Cubic Solver"))
        self.prompt.setText(_translate("MainWindow", "Choose the order of polynomial you would like to solve:"))
        self.lineSolve_btn.setText(_translate("MainWindow", "Solve"))
        self.Linearprompt.setText(_translate("MainWindow",
                                             "Please input your linear equation in the form: Y = aX + b, where a and b are constants "))
        self.quadinputprompt_2.setText(_translate("MainWindow", "Y =     X +     "))
        self.Alineinput.setPlaceholderText(_translate("MainWindow", "a"))
        self.Blineinput.setPlaceholderText(_translate("MainWindow", "b"))
        self.quadsolve_btn.setText(_translate("MainWindow", "Solve"))
        self.Quadraticprompt.setText(_translate("MainWindow",
                                                "Please input your quadratic equation in the form: Y = aX² + bX +c, where a, b and c are constants "))
        self.quadinputprompt.setText(_translate("MainWindow", "Y =      X² +      X + "))
        self.Aquadinput.setPlaceholderText(_translate("MainWindow", "a"))
        self.Bquadinput.setPlaceholderText(_translate("MainWindow", "b"))
        self.Cquadinput.setPlaceholderText(_translate("MainWindow", "c"))
        self.cubesolve_btn.setText(_translate("MainWindow", "Solve"))
        self.Cubicprompt.setText(_translate("MainWindow",
                                            "Please input your cubic equation in the form: Y = aX³ + bX² + cx + d, where a, b, c and d are constants "))
        self.cubeinputprompt.setText(_translate("MainWindow", "Y =      X³+      X²+      X+"))
        self.Acubeinput.setPlaceholderText(_translate("MainWindow", "a"))
        self.Bcubeinput.setPlaceholderText(_translate("MainWindow", "b"))
        self.Ccubeinput.setPlaceholderText(_translate("MainWindow", "c"))
        self.Dcubeinput.setPlaceholderText(_translate("MainWindow", "d"))
        self.Solutionprompt.setText(_translate("MainWindow", "The solution to your equation is:"))
        self.rootslabel.setText(_translate("MainWindow", "Roots: "))
        self.yinterceptlabel.setText(_translate("MainWindow", "Y-Intercept:"))
        self.turningpointslabel.setText(_translate("MainWindow", "Turning points:"))
