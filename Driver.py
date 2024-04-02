from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

token_numero = {
    1: "COMMENT",
    2: "PROGRAM",
    3: "INTEGER",
    4: "BOOLEAN",
    5: "BEGIN",
    6: "END",
    7: "WHILE",
    8: "DO",
    9: "READ",
    10: "VAR",
    11: "FALSE",
    12: "TRUE",
    13: "WRITE",
    14: "IF",
    15: "THEN",
    16: "ELSE",
    17: "INT",
    18: "OPAD",
    19: "OPMULT",
    20: "OPREL",
    21: "OPLOG",
    22: "OPNEG",
    23: "PVIG",
    24: "PONTO",
    25: "DPONTOS",
    26: "VIG",
    27: "ABPAR",
    28: "FPAR",
    29: "ATRIB",
    30: "CADEIA",
    31: "WS",
    32: "ID",
}


def main(argv):
    input_stream = FileStream(argv)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tokens = lexer.getAllTokens()

    erro = False

    for token in tokens:
        if token_numero[token.type] == "ID" and len(token.text) > 16:
            print(f"Erro palavra {token.text} tem mais de 16 caracteres")
            erro = True

    if not erro:
        for token in tokens:
            print(f"Tipo {token_numero[token.type]}, Nome {token.text} , Tamanho {len(token.text)}")

    tree = parser.prog()


if __name__ == '__main__':
    main("teste.txt")
