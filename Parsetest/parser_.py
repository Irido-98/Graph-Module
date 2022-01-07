# The underscore is because a builtin file has the name parser and this avoids complications

from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):  # If invalid syntax
        raise Exception('Invalid Syntax')

    def advance(self):  # Advance to next token
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):  # Check tokens against grammar rules
        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:  # If there still is a token after checking with rules, it is an error so raise error 
            self.raise_error()
        return result

    def expr(self):  # Lowest level rule, checks for add and minus symbols
        result = self.term()  # Checks for terms already in tree

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):  # Mid level rule, checks for multiply and divide symbols
        result = self.factor()  # Checks for factors

        while self.current_token is not None and self.current_token.type in (TokenType.INDICES, TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.INDICES:
                self.advance()
                result = IndiceNode(result, self.factor())
            elif self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):  # Highest level rule, checks for numbers
        token = self.current_token  # Checks for numbers

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()

            self.advance()
            return result

        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.MINUS:  # Check if number is negative and then output it as negative
            self.advance()
            return MinusNode(self.factor())

        self.raise_error()
