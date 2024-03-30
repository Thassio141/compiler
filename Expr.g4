grammar Expr;
import lexerExpr;

start_: PROGRAM ID bloco END;

bloco: decl_vars comandos;

decl_vars: var_decl (';' var_decl)* ';';

var_decl: tipo ID;

tipo: INTEGER | BOOLEAN;

comandos: comando (';' comando)* ';';

comando:
    atrib
    | leitura
    | escrita
    | condicional
    | loop;

atrib: ID ATRIB expr;

leitura: READ '(' ID ')';

escrita: WRITE '(' expr ')';

condicional: IF expr THEN comandos ENDIF;

loop: WHILE expr DO comandos ENDWHILE;

expr: expr_simples (OPREL expr_simples)?;

expr_simples:
    OPNEG expr_simples
    | CTE
    | ID
    | '(' expr ')';