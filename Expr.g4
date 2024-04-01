grammar Expr;

import lexerExpr;

prog: PROGRAM ID PVIG decls cmdComp PONTO;

decls: VAR listDecl | ;

listDecl: declTip | declTip VIG listDecl;

declTip: listId DPONTOS tip PVIG;

listId: ID | ID VIG listId;

tip: INTEGER | BOOLEAN | CADEIA;

cmdComp: BEGIN listCmd END;

listCmd: cmd | cmd PVIG listCmd;

cmd:
  cmdIf
  | cmdWhile
  | cmdRead
  | cmdWrite
  | cmdAtrib
  | cmdComp;

cmdIf: IF expr THEN cmd | IF expr THEN cmd ELSE cmd;

cmdWhile: WHILE expr DO cmd;

cmdRead: READ ABPAR listId FPAR;

cmdWrite: WRITE ABPAR listW FPAR;

listW: elemW | elemW VIG listW;

elemW: expr | CADEIA;

cmdAtrib: ID ATRIB expr ;

expr: minExpr | minExpr (OPREL) minExpr;

minExpr: term | term (OPAD) minExpr;

term: fat (OPMULT) term | fat;

fat: ID | INT | ABPAR expr FPAR | TRUE | FALSE | OPNEG fat;
