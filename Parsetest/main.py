from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        # Let user input stuff
        text = input('calc >> ')
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)
