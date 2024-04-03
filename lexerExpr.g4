lexer grammar lexerExpr;

COMMENT: '//' ~[/\r\n]* -> skip;

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
IF: 'IF';
THEN: 'THEN';
ELSE: 'ELSE';

OPAD: '+' | '-';
OPMULT: '*' | '/';

OPREL: '>' | '<' | '>=' | '<=' | '==' | '<>';

OPLOG: 'OR' | 'AND';

OPNEG: '~';

PVIG: ';';
PONTO: '.';
DPONTOS: ':';
VIG: ',';
ABPAR: '(';
FPAR: ')';
ATRIB: ':=';

CADEIA: '\'' ('\'\'' | ~ ('\''))* '\'';

WS: [ \t\r\n]+ -> skip;

ID: [a-zA-Z][a-zA-Z0-9]*;

CTE: [+-]?[0-9]+;