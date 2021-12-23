from fractions import Fraction
import math
import numpy as np

# User inputs equation 1
a1 = float(Fraction(input('Equation 1, Coefficient of x^3: ')))
b1 = float(Fraction(input('Equation 1, Coefficient of x^2: ')))
c1 = float(Fraction(input('Equation 1, Coefficient of x: ')))
d1 = float(Fraction(input('Equation 1, Coefficient of constant: ')))

# User inputs equation 2
a2 = float(Fraction(input('Equation 2, Coefficient of x^3: ')))
b2 = float(Fraction(input('Equation 2, Coefficient of x^2: ')))
c2 = float(Fraction(input('Equation 2, Coefficient of x: ')))
d2 = float(Fraction(input('Equation 2, Coefficient of constant: ')))

# Finding the resultant equation
x3 = a1 - a2
x2 = b1 - b2
x = c1 - c2
c = d1 - d2

if x3 == 0 and x2 == 0 and x == 0 and c == 0:
    print('Infinite roots')

while x3 != 0 or x2 != 0 or x != 0 or c != 0:
    # If the resultant equation is linear
    if x3 == 0 and x2 == 0:
        x_inter = round((c / -x), 3)
        y_inter = round((a1 * x_inter ** 3 + b1 * x_inter ** 2 + c1 * x_inter + d1), 3)
        print(f'Intersection: {x_inter},{y_inter}')

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
            print(f'Intersection: ({xinter1},{yinter1}), ({xinter2},{yinter2})')

        elif dis == 0:
            xinter = round((-x / (2 * x2)), 3)
            yinter = round((a1 * xinter ** 3 + b1 * xinter ** 2 + c1 * xinter + d1), 3)
            print(f'Intersection: {xinter},{yinter}')

        # If roots are complex, that means no intersection between the 2 equations inputted
        elif dis < 0:
            print('No intersection')

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
                print(f'Intersection: {inter}')
                break

            elif len(realarr) == 3:

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

                print(f'Intersections: {inter1}, {inter2}, {inter3}')
                break
    break
