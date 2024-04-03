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
  | cmdComp
  | cmdIfElse;

cmdIf: IF expr THEN cmd;

cmdIfElse: IF expr THEN cmd ELSE cmd;

cmdWhile: WHILE expr DO cmd;

cmdRead: READ ABPAR listId FPAR;

cmdWrite: WRITE ABPAR listW FPAR;

listW: elemW | elemW VIG listW;

elemW: expr | CADEIA;

cmdAtrib: ID ATRIB expr;

expr: exprAd | exprAd (OPREL) exprAd;

exprAd: exprMult | exprMult (OPAD) exprAd;

exprMult: exprDif (OPMULT) exprMult | exprDif;

exprDif: ID | CTE | ABPAR expr FPAR | TRUE | FALSE | OPNEG exprDif;
