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

    # checking condition for discriminant
    if dis > 0:
        print(" distinct roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(" repeated roots")
        print(-b / (2 * a))

        # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val / (2 * a))
        print(- b / (2 * a), " - i", sqrt_val / (2 * a))

        # If a is 0, then incorrect equation
    if a == 0:
        print("Run linear solver")


quadratic(a, b, c)
