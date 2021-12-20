from fractions import Fraction
import math
import numpy as np


def linear(a, b):
    # When gradient isn't 0
    while a != 0:
        x_root = (b / -a)
        # Since -0.0 is not correct math syntax
        if x_root == -0.0:
            x_root = 0.0
        y_root = 0.0
        print(x_root, y_root)
    # If gradient is 0, check if it crosses x-axes
    if a == 0 and b == 0:
        print('infinite roots')
    elif a == 0:
        print('no roots')


def quadratic(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

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
            root1 = str(round(- b / (2 * a), 3)) + '+' + str(round(sqrt_val / (2 * a), 3)) + 'i'
            root2 = str(round(- b / (2 * a), 3)) + '-' + str(round(sqrt_val / (2 * a), 3)) + 'i'
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

    elif a != 0:
        # Function only takes in arrays
        coeff = [a, b, c, d]
        # Using numpy to find the roots and then rounding them to 3 decimal places
        roots = np.roots(coeff)
        roundedroots = np.around(roots, 3)
        # Outputting the roots as a string
        stringroots = np.array2string(roundedroots)
        print(stringroots)


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
