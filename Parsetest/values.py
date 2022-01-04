from dataclasses import dataclass


# This will hold the value types the interpreter it able to produce
@dataclass
class Number:
    value: float

    def __repr__(self):
        return f'{self.value}'

