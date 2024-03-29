grammar Sintatico;

options {
  language = Python;
  output = AST;
}

// Regra inicial
programa: expressao EOF;

expressao:
  INT
  | IDENT
  | expressao OP_SUM expressao
  | expressao OP_SUB expressao
  ;
