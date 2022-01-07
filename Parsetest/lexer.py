from tokens import Token, TokenType


WHITESPACE = ' \n\t'  # What stuff will be ignored when iterating through
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)  # iter makes an object an iterator and allows us to choose the next object in the text
        self.advance()  # Advances to the first character

    def advance(self):  # Tracks current character and then moves onto the next character
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):  # Generate tokens from input
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()  # If character is whitespace, skip it
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()  # If character is digit or decimal point, run next method
            elif self.current_char == '+':  # Specific token is generated if specific input 
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*' or self.current_char == 'x':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.INDICES)
            else:
                raise Exception(f'Illegal Character {self.current_char}')

    def generate_number(self):  # Adds number to token
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':  # Check for multiple decimal points and stop if there are more than 1
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):  # If number ends in decimal or starts with decimal, add a 0 infront or behind it
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))  # Return number as token
