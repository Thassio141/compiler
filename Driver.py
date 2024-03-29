import token

from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

token_numero_para_nome = {
    1: "T__0",
    2: "T__1",
    3: "T__2",
    4: "T__3",
    5: "T__4",
    6: "T__5",
    7: "T__6",
    8: "T__7",
    9: "INT",
    10: "WS"
}

def main(argv):
    input_stream = FileStream(argv)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    for token in lexer.getAllTokens():
        print(f"Tipo {token_numero_para_nome[token.type]}, Nome {token.text}")
    tree = parser.start_()

if __name__ == '__main__':
    main("teste.txt")