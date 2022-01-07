from enum import Enum
from dataclasses import dataclass


# Define all types of tokens
class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    INDICES = 7


@dataclass  # This is a decorator that allows us to hold different values
class Token:  # Class for the info about the individual token
    type: TokenType
    value: any = None

    def __repr__(self):  # Representation method for debugging if printing a token
        return self.type.name + (f":{self.value}" if self.value is not None else "")
