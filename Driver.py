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
    17: "OPAD",
    18: "OPMULT",
    19: "OPREL",
    20: "OPLOG",
    21: "OPNEG",
    22: "PVIG",
    23: "PONTO",
    24: "DPONTOS",
    25: "VIG",
    26: "ABPAR",
    27: "FPAR",
    28: "ATRIB",
    29: "CADEIA",
    30: "WS",
    31: "ID",
    32: "CTE"
}


def main(argv):
    input_stream = FileStream(argv)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tokens = lexer.getAllTokens()

    for token in tokens:
        if token.type == 31 and len(token.text) > 16:
            raise ValueError(f"Erro ID {token.text} tem mais de 16 caracteres")
        elif token.type == 32:
            if int(token.text) > 32767 or int(token.text) < -32768:
                raise ValueError(f"Erro CTE {token.text} é maior que 2 bytes")

    for token in tokens:
        print(f"Tipo {token_numero[token.type]}, Nome {token.text} , Tamanho {len(token.text)}")

    tree = parser.prog()


if __name__ == '__main__':
    main("teste.txt")
