from fractions import Fraction
import math
import numpy as np


def linear(a, b):
    # When gradient isn't 0
    y_intercept = (0.0, b)
    while a != 0:
        x_root = (b / -a)
        # Since -0.0 is not correct math syntax
        if x_root == -0.0:
            x_root = 0.0
        y_root = 0.0

        print('The roots are: ', x_root, y_root)
        print('Y-intercept is: ', y_intercept)
        break
    # If gradient is 0, check if it crosses x-axes
    if a == 0 and b == 0:
        print('infinite roots')
        print('Y-intercept is: ', y_intercept)
    elif a == 0:
        print('no roots')
        print('Y-intercept is: ', y_intercept)


def quadratic(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    y_intercept = (0.0, c)

    # Differential of quadratic
    x = 2 * a
    y = b

    # Finding the roots of the differential
    dx_root = round((y / -x), 3)

    # Since -0.0 is not correct math syntax
    if dx_root == -0.0:
        dx_root = 0.0

    dy_root = round((a * (dx_root ** 2) + b * dx_root + c), 3)
    turnpoint = (dx_root, dy_root)

    # Checking if turning point is max or min and outputting y-intercept
    if a / abs(a) == 1:
        print('Turning point is a minimum at: ', turnpoint)
    elif a / abs(a) == -1:
        print('Turning point is a maximum at: ', turnpoint)
    print('Y-intercept at: ', y_intercept)

    if a != 0:
        # checking condition for discriminant
        if dis > 0:
            root1 = (round((-b + sqrt_val) / (2 * a), 3), 0.0)
            root2 = (round((-b - sqrt_val) / (2 * a), 3), 0.0)
            if root1 == (-0.0, 0.0):
                root1 = (0.0, 0.0)
            elif root2 == (-0.0, 0.0):
                root2 = (0.0, 0.0)
            print('Distinct roots at:', root1, root2)

        elif dis == 0:
            root = (round((-b / (2 * a)), 3), 0.0)
            if root == (-0.0, 0.0):
                root = (0.0, 0.0)
            print('Repeated root at:', root)

        # when discriminant is less than 0. Complex roots
        else:
            root1 = str(round(- b / (2 * a), 3)) + '+' + str(round(sqrt_val / (2 * a), 3)) + 'j'
            root2 = str(round(- b / (2 * a), 3)) + '-' + str(round(sqrt_val / (2 * a), 3)) + 'j'
            print('Complex roots at:', root1 + ' and ' + root2)

    # If a is 0, then tell user to use linear solver
    if a == 0:
        print("You inputted a linear equation. To solve this, run the linear solver")


def cubic(a, b, c, d):
    # Check to see input is actually a cubic
    if a == 0 and b != 0:
        print('Run the quadratic solver ')
    elif a == 0 and b == 0:
        print('Run the linear solver')

    y_intercept = (0.0, d)

    # First order differential
    x = 3 * a ** 2
    y = 2 * b
    z = c
    dis = y * y - 4 * x * z
    sqrt_val = math.sqrt(abs(dis))

    if dis > 0:
        turnx1 = round((-y + sqrt_val) / (2 * x), 3)
        turnx2 = round((-y - sqrt_val) / (2 * x), 3)
        if turnx1 == -0.0:
            turnx1 = 0.0
        elif turnx2 == -0.0:
            turnx2 = 0.0
        turny1 = round((a*turnx1**3)+(b*turnx1**2)+(c*turnx1)+d, 3)
        turny2 = round(((a * turnx2 ** 3) + (b * turnx2 ** 2) + (c * turnx2) + d), 3)
        turnpoint1 = (turnx1, turny1)
        turnpoint2 = (turnx2, turny2)
        print('Turning points at: ', turnpoint1, turnpoint2)

    elif dis == 0:
        inflectionx = round((-y / (2 * x)), 3)
        if inflectionx == -0.0:
            inflectionx = 0.0
        inflectiony = round((a*inflectionx**3)+(b*inflectionx**2)+(c*inflectionx)+d, 3)
        inflectionpoint = (inflectionx, inflectiony)
        print('Stationary point of inflection at: ', inflectionpoint)

    else:
        print('There is only a points of inflection, no turning points')


    if a != 0:
        # Function only takes in arrays
        coeff = [a, b, c, d]
        # Using numpy to find the roots and then rounding them to 3 decimal places
        roots = np.roots(coeff)
        roundedroots = np.around(roots, 3)
        # Outputting the roots as a string
        stringroots = np.array2string(roundedroots)
        print('Roots at: ', stringroots)
        print('Y-intercept at: ', y_intercept)


# This will let the user choose which solver they need and then input the required coefficients
while True:
    print('Input the number to choose the solver required: 1 - Linear, 2 - Quadratic, 3 - Cubic')
    solverchoice = int(input('Enter your choice'))
    if solverchoice == 1:
        # User inputs the gradient and the y-intercept
        a = float(Fraction(input('Enter coefficient of x: ')))
        b = float(Fraction(input('Enter constant: ')))
        c = 0
        d = 0
        linear(a, b)
        break
    elif solverchoice == 2:
        # User inputs the coefficients
        a = float(Fraction(input('Enter coefficient of x^2: ')))
        b = float(Fraction(input('Enter coefficient of x: ')))
        c = float(Fraction(input('Enter constant: ')))
        d = 0
        quadratic(a, b, c)
        break
    elif solverchoice == 3:
        # User inputs the coefficients
        a = float(Fraction(input('Enter coefficient of x^3: ')))
        b = float(Fraction(input('Enter coefficient of x^2: ')))
        c = float(Fraction(input('Enter coefficient of x: ')))
        d = float(Fraction(input('Enter constant: ')))
        cubic(a, b, c, d)
        break
    else:
        print("You didn't choose 1,2 or 3")
