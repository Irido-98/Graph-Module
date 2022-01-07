from dataclasses import dataclass


@dataclass
class NumberNode:  # Stores the value of the number
    value: float

    def __repr__(self):  # Returns value as string
        return f'{self.value}'


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}+{self.node_b})'


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}-{self.node_b})'


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}*{self.node_b})'


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}/{self.node_b})'


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f'(+{self.node})'


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f'(-{self.node})'


@dataclass
class IndiceNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}**{self.node_b})'
