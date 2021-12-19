from fractions import Fraction
import math

# User inputs the gradient and the y-intercept
a = float(Fraction(input('Enter coefficient of x (gradient): ')))

b = float(Fraction(input('Enter y-intercept: ')))


def linear(a, b):
    # When gradient isn't 0
    while a != 0:
        x_root = (b / -a)
        # Since -0.0 is not correct math syntax
        if x_root == -0.0:
            x_root = 0.0

        y_root = a * x_root + b

        return x_root, y_root
    # If gradient is 0, check if it crosses x-axes
    if a == 0 and b == 0:
        return 'infinite roots'
    elif a == 0:
        return 'no roots'


linear(a, b)


# User inputs the gradient and the y-intercept
a = float(Fraction(input('Enter coefficient of x^2: ')))

b = float(Fraction(input('Enter coefficient of x: ')))

c = float(Fraction(input('Enter constant: ')))


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


quadratic(a, b, c)
