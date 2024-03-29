lexer grammar Lexico;

// Ignorar espaços em branco
WHITESPACE: [ \t\r\n]+ -> skip;

// Tokens
IDENT: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
OP_SUM: '+';
OP_SUB: '-';