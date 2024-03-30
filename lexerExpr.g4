lexer grammar lexerExpr;

// Regras de tokens

// Palavras reservadas
PROGRAM: 'PROGRAM';
INTEGER: 'INTEGER';
BOOLEAN: 'BOOLEAN';
BEGIN: 'BEGIN';
END: 'END';
WHILE: 'WHILE';
DO: 'DO';
READ: 'READ';
VAR: 'VAR';
FALSE: 'FALSE';
TRUE: 'TRUE';
WRITE: 'WRITE';

// Operadores aritméticos
OPAD: '+' | '-';
OPMULT: '*' | '/';

// Operadores relacionais
OPREL: '>' | '<' | '>=' | '<=' | '==' | '<>';

// Operadores lógicos
OPLOG: 'OR' | 'AND';

// Operador de negação
OPNEG: '~';

// Símbolos
PVIG: ';';
PONTO: '.';
DPONTOS: ':';
VIG: ',';
ABPAR: '(';
FPAR: ')';
ATRIB: ':=';

// Identificadores e constantes
ID: [a-zA-Z][a-zA-Z0-9_]*;
CTE: [0-9]+;

// Comentários
COMMENT: '//'.*'\n';

// Espaços em branco
WS: [ \t\r\n]+ -> skip;

// Ignorar outros caracteres
OTHER: .;