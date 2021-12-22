from fractions import Fraction
import math
import numpy as np

a1 = float(Fraction(input('Equation 1, Coefficient of x^3: ')))
b1 = float(Fraction(input('Equation 1, Coefficient of x^2: ')))
c1 = float(Fraction(input('Equation 1, Coefficient of x: ')))
d1 = float(Fraction(input('Equation 1, Coefficient of constant: ')))

a2 = float(Fraction(input('Equation 2, Coefficient of x^3: ')))
b2 = float(Fraction(input('Equation 2, Coefficient of x^2: ')))
c2 = float(Fraction(input('Equation 2, Coefficient of x: ')))
d2 = float(Fraction(input('Equation 2, Coefficient of constant: ')))

# Finding the resultant equation
x3 = a1 - a2
x2 = b1 - b2
x = c1 - c2
c = d1 - d2

# If the resultant equation is linear
if x3 == 0 and x2 == 0:
    x_inter = round((c / -x), 3)
    y_inter = round((a1 * x_inter ** 3 + b1 * x_inter ** 2 + c1 * x_inter + d1), 3)
    print(f'Intersection: ({x_inter},{y_inter})')

# If the resultant equation is quadratic
elif x3 == 0:
    dis = x * x - 4 * x2 * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        xinter1 = round((-x + sqrt_val) / (2 * x2), 3)
        yinter1 = round((a1 * xinter1 ** 3 + b1 * xinter1 ** 2 + c1 * xinter1 + d1), 3)
        xinter2 = round((-x - sqrt_val) / (2 * x2), 3)
        yinter2 = round((a1 * xinter2 ** 3 + b1 * xinter2 ** 2 + c1 * xinter2 + d1), 3)
        print(f'Intersection: ({xinter1},{yinter1}), ({xinter2},{yinter2})')

    elif dis == 0:
        xinter = round((-x / (2 * x2)), 3)
        yinter = round((a1 * xinter ** 3 + b1 * xinter ** 2 + c1 * xinter + d1), 3)
        print(f'Intersection: ({xinter},{yinter})')

    elif dis < 0:
        print('No intersection')

# If the resultant equation is cubic
elif x3 != 0:
    coeff = [x3, x2, x, c]
    # Using numpy to find the roots and then rounding them to 3 decimal places
    intersection = np.roots(coeff)
    roundedinter = np.around(intersection, 3)
    # Outputting the roots as a string
    stringinter = np.array2string(roundedinter)
    print(f'Intersection: {stringinter}')
