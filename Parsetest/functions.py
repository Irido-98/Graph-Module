class function:
    def pow(self, base, exponent):
        return base ** exponent

    def faktorial(self, n):
        value = float(1)
        for i in range(1, n + 1):
            value = value * i
        return value

    def sin(self, x):
        x = x * 3.14 / 180
        value = x
        sign = -1
        n = 200  # precision
        i = 3
        while i < n:
            value = value + (self.pow(x, i) / self.faktorial(i) * sign)
            i = i + 2
            sign = sign * -1
        return value

    def cos(self, x):
        x = x * 3.14 / 180
        value = 1
        sign = -1
        n = 200  # precision
        i = 2
        while i < n:
            value = value + (self.pow(x, i) / self.faktorial(i) * sign)
            i = i + 2
            sign = sign * -1

        return value

    def tan(self, x):
        value = self.sin(x)/self.cos(x)
        return value
